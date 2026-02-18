"""Scheduler Agent — generates phased cooking timeline."""

import logging
import time

from pydantic import BaseModel

from app.agents.base import AgentContext, AgentTrace
from app.prompts.scheduler import SCHEDULER_SYSTEM, SCHEDULER_USER
from app.schemas.plan import TimelinePhase
from app.services.llm.base import LLMService

logger = logging.getLogger(__name__)


class SchedulerOutput(BaseModel):
    timeline: list[TimelinePhase]
    total_time_minutes: int
    active_time_minutes: int


async def run_scheduler(ctx: AgentContext, llm: LLMService) -> AgentContext:
    start = time.monotonic()
    constraints = ctx.constraints

    # Format ingredients for the prompt
    ingredients_text = "\n".join(
        f"- {ing.name}: {ing.amount_grams}g ({ing.original_amount})"
        for ing in ctx.ingredients_list
    )

    # Build capabilities string
    cap_list = []
    if constraints:
        for field_name in constraints.model_fields:
            val = getattr(constraints, field_name)
            if isinstance(val, bool) and val:
                cap_list.append(field_name.replace("_", " "))

    user_prompt = SCHEDULER_USER.format(
        dish_name=ctx.dish_name,
        dish_description=ctx.dish_description,
        ingredients=ingredients_text,
        time_limit=ctx.audit_request.time_limit_minutes,
        active_minutes=constraints.max_active_minutes if constraints else int(ctx.audit_request.time_limit_minutes * 0.7),
        skill_level=ctx.audit_request.user_skill,
        capabilities=", ".join(cap_list) if cap_list else "Basic stovetop cooking",
    )

    result = await llm.generate(
        system_prompt=SCHEDULER_SYSTEM,
        user_prompt=user_prompt,
        response_model=SchedulerOutput,
        temperature=0.6,
    )

    # Post-validate: no task exceeds total time limit
    for phase in result.timeline:
        for task in phase.tasks:
            if task.duration_minutes > ctx.audit_request.time_limit_minutes:
                task.duration_minutes = ctx.audit_request.time_limit_minutes
                logger.warning(
                    f"Task '{task.description}' duration capped to time limit"
                )

    ctx.timeline = result.timeline
    ctx.total_time_minutes = result.total_time_minutes
    ctx.active_time_minutes = result.active_time_minutes

    elapsed_ms = int((time.monotonic() - start) * 1000)
    ctx.trace.append(AgentTrace(
        agent_name="Scheduler",
        input_summary=f"Dish: {ctx.dish_name}",
        output_summary=f"{len(result.timeline)} phases, {result.total_time_minutes}min total",
        latency_ms=elapsed_ms,
    ))

    return ctx
