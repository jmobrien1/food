from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Technique(Base):
    __tablename__ = "techniques"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    min_skill_level: Mapped[str] = mapped_column(String(50), nullable=False)
    required_equipment: Mapped[str | None] = mapped_column(String(200))
    time_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    pro_tip: Mapped[str | None] = mapped_column(Text)
    fallback_technique_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("techniques.id")
    )
