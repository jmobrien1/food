from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_session
from app.schemas.common import HealthResponse, ReadinessResponse
from app.services.llm.factory import get_llm_service

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok")


@router.get("/health/ready", response_model=ReadinessResponse)
async def readiness(session: AsyncSession = Depends(get_session)):
    # Check database
    db_status = "ok"
    try:
        await session.execute(text("SELECT 1"))
    except Exception:
        db_status = "unavailable"

    # Check LLM
    llm_status = "ok"
    try:
        llm = get_llm_service(settings)
        if hasattr(llm, "check_connectivity"):
            if not await llm.check_connectivity():
                llm_status = "unavailable"
    except Exception:
        llm_status = "unavailable"

    overall = "ok" if db_status == "ok" and llm_status == "ok" else "degraded"
    return ReadinessResponse(status=overall, database=db_status, llm=llm_status)
