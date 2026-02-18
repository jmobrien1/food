"""Executive Chef Agent — reviews plan and adds Chef's Secrets."""

import logging
import time

from pydantic import BaseModel

from app.agents.base import AgentContext, AgentTrace
from app.prompts.executive_chef import EXECUTIVE_CHEF_SYSTEM, EXECUTIVE_CHEF_REVIEW
from app.schemas.plan import ChefSecret, TimelineTask
from app.services.llm.base import LLMService

logger = logging.getLogger(__name__)


class ExecChefOutput(BaseModel):
    chefs_secrets: list[ChefSecret]
    additional_tasks: list[TimelineTask] = []
    review_notes: list[str] = []


async def run_executive_chef(ctx: AgentContext, llm: LLMService) -> AgentContext:
    start = time.monotonic()

    # Format data for prompt
    ingredients_text = "\n".join(
        f"- {ing.name}: {ing.amount_grams}g" for ing in ctx.ingredients_list
    )

    timeline_text = ""
    for phase in ctx.timeline:
        timeline_text += f"\n**{phase.phase}:**\n"
        for task in phase.tasks:
            active_tag = "ACTIVE" if task.is_active else "PASSIVE"
            timeline_text += f"  {task.step}. [{active_tag}] {task.description} ({task.duration_minutes}min)\n"

    user_prompt = EXECUTIVE_CHEF_REVIEW.format(
        dish_name=ctx.dish_name,
        dish_description=ctx.dish_description,
        ingredients=ingredients_text,
        timeline=timeline_text,
        skill_level=ctx.audit_request.user_skill,
    )

    result = await llm.generate(
        system_prompt=EXECUTIVE_CHEF_SYSTEM,
        user_prompt=user_prompt,
        response_model=ExecChefOutput,
        temperature=0.7,
    )

    ctx.chefs_secrets = result.chefs_secrets

    # Add any additional timeline tasks from the chef
    if result.additional_tasks and ctx.timeline:
        # Append to the last phase (Active Cooking)
        last_phase = ctx.timeline[-1]
        max_step = max(t.step for t in last_phase.tasks) if last_phase.tasks else 0
        for task in result.additional_tasks:
            task.step = max_step + 1
            max_step += 1
            last_phase.tasks.append(task)

    elapsed_ms = int((time.monotonic() - start) * 1000)
    ctx.trace.append(AgentTrace(
        agent_name="Executive Chef",
        input_summary=f"Reviewing: {ctx.dish_name}",
        output_summary=f"{len(result.chefs_secrets)} secrets, {len(result.review_notes)} notes",
        latency_ms=elapsed_ms,
    ))

    return ctx
