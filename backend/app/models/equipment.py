from sqlalchemy import Boolean, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Equipment(Base):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    is_professional: Mapped[bool] = mapped_column(Boolean, default=False)
    capabilities: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    home_alt: Mapped[str | None] = mapped_column(String(200))
