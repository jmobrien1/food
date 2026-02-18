import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.orchestrator import run_pipeline
from app.core.config import settings
from app.core.database import get_session
from app.models.plan_history import PlanHistory
from app.schemas.audit import AuditRequest
from app.schemas.plan import (
    ExecutionPlan,
    PlanGenerateRequest,
    PlanGenerateResponse,
    PlanGetResponse,
)
from app.services.llm.factory import get_llm_service

router = APIRouter(prefix="/plans", tags=["plans"])


@router.post("/generate", response_model=PlanGenerateResponse)
async def generate_plan(
    body: PlanGenerateRequest,
    session: AsyncSession = Depends(get_session),
):
    llm = get_llm_service(settings)
    audit_request = AuditRequest(
        ingredients=body.ingredients,
        equipment=body.equipment,
        time_limit_minutes=body.time_limit_minutes,
        user_skill=body.user_skill,
        guest_count=body.guest_count,
        intent=body.intent,
    )
    try:
        plan_id, plan = await run_pipeline(audit_request, session, llm)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Plan generation failed: {str(e)}")

    return PlanGenerateResponse(id=plan_id, plan=plan)


@router.get("/{plan_id}", response_model=PlanGetResponse)
async def get_plan(
    plan_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        uid = uuid.UUID(plan_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid plan ID format")

    stmt = select(PlanHistory).where(PlanHistory.id == uid)
    result = await session.execute(stmt)
    record = result.scalar_one_or_none()

    if not record:
        raise HTTPException(status_code=404, detail="Plan not found")

    plan = ExecutionPlan.model_validate(record.execution_plan)
    return PlanGetResponse(
        id=str(record.id),
        plan=plan,
        model_used=record.model_used,
        latency_ms=record.latency_ms,
    )
