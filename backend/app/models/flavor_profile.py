from sqlalchemy import Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class FlavorProfile(Base):
    __tablename__ = "flavor_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ingredients.id", ondelete="CASCADE"), nullable=False
    )
    descriptor: Mapped[str] = mapped_column(String(100), nullable=False)
    intensity: Mapped[float] = mapped_column(Float, nullable=False)

    ingredient: Mapped["Ingredient"] = relationship(back_populates="flavor_profiles")  # noqa: F821

    __table_args__ = (
        UniqueConstraint("ingredient_id", "descriptor", name="uq_flavor_profiles_ingredient_descriptor"),
    )
