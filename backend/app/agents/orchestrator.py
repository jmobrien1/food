"""Pipeline Orchestrator — runs all 4 agents sequentially and persists result."""

import logging
import time
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.auditor import run_audit
from app.agents.base import AgentContext
from app.agents.executive_chef import run_executive_chef
from app.agents.scheduler import run_scheduler
from app.agents.translator import run_translator
from app.models.plan_history import PlanHistory
from app.schemas.audit import AuditRequest
from app.schemas.plan import ExecutionPlan
from app.services.llm.base import LLMService

logger = logging.getLogger(__name__)


async def run_pipeline(
    request: AuditRequest,
    session: AsyncSession,
    llm: LLMService,
) -> tuple[str, ExecutionPlan]:
    """Run the full 4-agent pipeline and return (plan_id, plan)."""
    pipeline_start = time.monotonic()

    ctx = AgentContext(audit_request=request)

    # Phase 1: Audit (deterministic)
    logger.info("Running Auditor...")
    ctx = await run_audit(ctx, session)

    # Phase 2: Translation (LLM)
    logger.info("Running Translator...")
    ctx = await run_translator(ctx, session, llm)

    # Phase 3: Schedule (LLM)
    logger.info("Running Scheduler...")
    ctx = await run_scheduler(ctx, llm)

    # Phase 4: Executive Chef review (LLM)
    logger.info("Running Executive Chef...")
    ctx = await run_executive_chef(ctx, llm)

    # Build final plan
    plan = ctx.to_plan()

    total_ms = int((time.monotonic() - pipeline_start) * 1000)

    # Persist to plan_history
    plan_id = str(uuid.uuid4())
    history = PlanHistory(
        id=uuid.UUID(plan_id),
        audit_request=request.model_dump(),
        constraints=ctx.constraints.model_dump() if ctx.constraints else {},
        execution_plan=plan.model_dump(),
        agent_traces=[
            {
                "agent": t.agent_name,
                "input": t.input_summary,
                "output": t.output_summary,
                "latency_ms": t.latency_ms,
                "error": t.error,
            }
            for t in ctx.trace
        ],
        model_used=getattr(llm, "_model", "unknown"),
        latency_ms=total_ms,
    )
    session.add(history)
    await session.commit()

    logger.info(f"Pipeline complete in {total_ms}ms — plan_id={plan_id}")
    return plan_id, plan
