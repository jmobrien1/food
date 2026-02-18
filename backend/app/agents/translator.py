"""Translation Engine — core LLM agent for dish concept and ingredient list.

Retrieves culinary knowledge via pgvector, gets flavor affinities,
calls Claude to generate dish concept + ingredients, handles scaling.
"""

import logging
import time

from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.base import AgentContext, AgentTrace
from app.models.ingredient import Ingredient
from app.prompts.translator import TRANSLATOR_SYSTEM, TRANSLATOR_USER
from app.schemas.plan import PlanIngredient
from app.services.flavor_graph import get_affinities_for_ingredient
from app.services.knowledge_base import search_knowledge
from app.services.llm.base import LLMService
from app.services.scaling import scale_ingredient, compute_rcf

logger = logging.getLogger(__name__)


class TranslatorOutput(BaseModel):
    dish_name: str
    dish_description: str
    difficulty: str
    ingredients: list[PlanIngredient]
    substitution_notes: list[str] = []


async def run_translator(
    ctx: AgentContext, session: AsyncSession, llm: LLMService
) -> AgentContext:
    start = time.monotonic()
    req = ctx.audit_request
    constraints = ctx.constraints

    # Look up ingredient IDs for affinity queries
    affinities_text = []
    for ing_name in req.ingredients[:6]:  # Top 6 for affordability
        stmt = select(Ingredient).where(func.lower(Ingredient.name) == ing_name.lower())
        result = await session.execute(stmt)
        ing = result.scalar_one_or_none()
        if ing:
            affs = await get_affinities_for_ingredient(session, ing.id, min_score=0.5, limit=5)
            for a in affs:
                affinities_text.append(
                    f"  {ing_name} + {a['ingredient_name']}: {a['affinity_score']:.2f}"
                )

    # Semantic search for relevant culinary knowledge
    knowledge_text = ""
    intent = req.intent or f"dish with {', '.join(req.ingredients[:4])}"
    try:
        async with session.begin_nested():
            knowledge = await search_knowledge(session, llm, intent, top_k=3)
            knowledge_text = "\n".join(
                f"- {k['text_content'][:200]}" for k in knowledge
            )
    except Exception as e:
        logger.warning(f"Knowledge base search failed: {e}")
        knowledge_text = "(No knowledge base results available)"

    # Build capabilities string
    cap_list = []
    if constraints:
        for field_name in constraints.model_fields:
            val = getattr(constraints, field_name)
            if isinstance(val, bool) and val:
                cap_list.append(field_name.replace("_", " "))

    # Call LLM
    user_prompt = TRANSLATOR_USER.format(
        ingredients=", ".join(req.ingredients),
        capabilities=", ".join(cap_list) if cap_list else "Basic stovetop cooking",
        skill_level=req.user_skill,
        skill_tier=constraints.skill_tier if constraints else 2,
        time_limit=req.time_limit_minutes if req.time_limit_minutes > 0 else "unlimited",
        active_minutes=constraints.max_active_minutes if constraints else int((req.time_limit_minutes or 1440) * 0.7),
        guest_count=req.guest_count,
        intent=intent,
        affinities="\n".join(affinities_text) if affinities_text else "  (No affinity data available)",
        knowledge=knowledge_text or "  (No additional knowledge)",
    )

    result = await llm.generate(
        system_prompt=TRANSLATOR_SYSTEM,
        user_prompt=user_prompt,
        response_model=TranslatorOutput,
        temperature=0.8,
    )

    # Apply scaling if guest count != 4 (base serving)
    if req.guest_count != 4:
        rcf = compute_rcf(req.guest_count, base_servings=4)
        scaled_ingredients = []
        for ing in result.ingredients:
            # Look up scaling info from DB
            stmt = select(Ingredient).where(func.lower(Ingredient.name) == ing.name.lower())
            db_result = await session.execute(stmt)
            db_ing = db_result.scalar_one_or_none()

            if db_ing and db_ing.is_potent:
                scaled = scale_ingredient(
                    name=ing.name,
                    base_grams=ing.amount_grams,
                    rcf=rcf,
                    scaling_exponent=db_ing.scaling_exponent,
                    is_potent=True,
                    safety_ceiling=db_ing.safety_ceiling,
                )
                ing.amount_grams = scaled.scaled_grams
                ing.scaling_notes = f"Scaled {scaled.scaling_method} for {req.guest_count} servings"
            else:
                ing.amount_grams = round(ing.amount_grams * rcf, 1)

            scaled_ingredients.append(ing)
        result.ingredients = scaled_ingredients

    ctx.dish_name = result.dish_name
    ctx.dish_description = result.dish_description
    ctx.difficulty = result.difficulty
    ctx.ingredients_list = result.ingredients
    ctx.substitution_notes = result.substitution_notes

    elapsed_ms = int((time.monotonic() - start) * 1000)
    ctx.trace.append(AgentTrace(
        agent_name="Translator",
        input_summary=f"{len(req.ingredients)} ingredients, intent='{intent[:50]}'",
        output_summary=f"Dish: {result.dish_name}, {len(result.ingredients)} ingredients",
        latency_ms=elapsed_ms,
    ))

    return ctx
