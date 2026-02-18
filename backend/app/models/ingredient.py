from sqlalchemy import Boolean, Float, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)
    subcategory: Mapped[str | None] = mapped_column(String(100))
    is_potent: Mapped[bool] = mapped_column(Boolean, default=False)
    scaling_exponent: Mapped[float] = mapped_column(Float, default=1.0)
    safety_ceiling: Mapped[float | None] = mapped_column(Float)

    flavor_profiles: Mapped[list["FlavorProfile"]] = relationship(  # noqa: F821
        back_populates="ingredient", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("ix_ingredients_name_trgm", "name", postgresql_using="gin",
              postgresql_ops={"name": "gin_trgm_ops"}),
    )
