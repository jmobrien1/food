from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_session
from app.services.llm.factory import get_llm_service


def get_db() -> AsyncSession:  # type: ignore[misc]
    return Depends(get_session)


def get_llm():
    return get_llm_service(settings)
