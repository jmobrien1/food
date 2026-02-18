import uuid

from sqlalchemy import Float, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.models.base import Base


class PlanHistory(Base):
    __tablename__ = "plan_history"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    audit_request: Mapped[dict] = mapped_column(JSONB, nullable=False)
    constraints: Mapped[dict] = mapped_column(JSONB, nullable=False)
    execution_plan: Mapped[dict] = mapped_column(JSONB, nullable=False)
    agent_traces: Mapped[dict | None] = mapped_column(JSONB)
    model_used: Mapped[str] = mapped_column(String(100), nullable=False)
    latency_ms: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at = mapped_column(server_default=func.now())
