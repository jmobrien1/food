"""Auditor Agent — mostly deterministic constraint mapping.

Maps equipment to capability flags, validates ingredients against DB,
and flags impossible scenarios.
"""

import logging

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.base import AgentContext, AgentTrace
from app.models.equipment import Equipment
from app.models.ingredient import Ingredient
from app.schemas.audit import ConstraintFlags

logger = logging.getLogger(__name__)

SKILL_MAP = {
    "Home Cook": 1,
    "Ambitious Amateur": 2,
    "Serious Enthusiast": 3,
}

# Equipment name patterns → capability flags
CAPABILITY_RULES: dict[str, list[str]] = {
    "cast iron": ["can_sear_high_heat"],
    "carbon steel": ["can_sear_high_heat"],
    "stainless steel pan": ["can_sear_high_heat"],
    "oven": ["can_oven_roast"],
    "dutch oven": ["can_oven_roast", "can_deep_fry"],
    "immersion circulator": ["can_sous_vide"],
    "sous vide": ["can_sous_vide"],
    "deep fryer": ["can_deep_fry"],
    "smoker": ["can_smoke"],
    "grill": ["can_smoke", "can_sear_high_heat"],
    "torch": ["can_torch"],
    "kitchen torch": ["can_torch"],
    "blender": ["has_blender"],
    "immersion blender": ["has_blender"],
    "food processor": ["has_food_processor"],
    "stand mixer": ["has_stand_mixer"],
}


async def run_audit(ctx: AgentContext, session: AsyncSession) -> AgentContext:
    """Run the auditor agent to map constraints."""
    import time
    start = time.monotonic()

    req = ctx.audit_request

    # Determine capabilities from equipment
    capabilities = set()
    for equip_name in req.equipment:
        equip_lower = equip_name.lower()
        # Check against rules
        for pattern, caps in CAPABILITY_RULES.items():
            if pattern in equip_lower:
                capabilities.update(caps)

        # Also check DB for capabilities (exact match first, then substring)
        stmt = select(Equipment).where(
            func.lower(Equipment.name) == equip_lower
        )
        result = await session.execute(stmt)
        db_equip = result.scalar_one_or_none()
        if db_equip and db_equip.capabilities:
            capabilities.update(db_equip.capabilities)

    # Skill tier
    skill_tier = SKILL_MAP.get(req.user_skill, 2)

    # Active time budget (70% of total for active work)
    max_active = int(req.time_limit_minutes * 0.7)

    ctx.constraints = ConstraintFlags(
        can_sous_vide="can_sous_vide" in capabilities,
        can_sear_high_heat="can_sear_high_heat" in capabilities,
        can_oven_roast="can_oven_roast" in capabilities,
        can_deep_fry="can_deep_fry" in capabilities,
        can_smoke="can_smoke" in capabilities,
        can_torch="can_torch" in capabilities,
        has_blender="has_blender" in capabilities,
        has_food_processor="has_food_processor" in capabilities,
        has_stand_mixer="has_stand_mixer" in capabilities,
        max_active_minutes=max_active,
        skill_tier=skill_tier,
        guest_count=req.guest_count,
    )

    # Validate ingredients exist in DB
    flags = []
    for ing_name in req.ingredients:
        stmt = select(Ingredient).where(
            func.lower(Ingredient.name) == ing_name.lower()
        )
        result = await session.execute(stmt)
        if not result.scalar_one_or_none():
            flags.append(f"Ingredient '{ing_name}' not in database — will use LLM knowledge")

    # Flag potential issues
    if req.time_limit_minutes < 30 and req.guest_count > 4:
        flags.append("Very tight timeline for guest count — consider simpler preparations")
    if skill_tier == 1 and req.time_limit_minutes < 45:
        flags.append("Home cook with tight timeline — will stick to simple techniques")

    ctx.flags = flags

    elapsed_ms = int((time.monotonic() - start) * 1000)
    ctx.trace.append(AgentTrace(
        agent_name="Auditor",
        input_summary=f"{len(req.ingredients)} ingredients, {len(req.equipment)} equipment",
        output_summary=f"Capabilities: {len(capabilities)}, Flags: {len(flags)}",
        latency_ms=elapsed_ms,
    ))

    return ctx
