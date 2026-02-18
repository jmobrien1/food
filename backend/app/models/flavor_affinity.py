from sqlalchemy import CheckConstraint, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class FlavorAffinity(Base):
    __tablename__ = "flavor_affinities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ingredient_a_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ingredients.id", ondelete="CASCADE"), nullable=False
    )
    ingredient_b_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ingredients.id", ondelete="CASCADE"), nullable=False
    )
    affinity_score: Mapped[float] = mapped_column(Float, nullable=False)
    source: Mapped[str | None] = mapped_column(String(200))

    __table_args__ = (
        UniqueConstraint("ingredient_a_id", "ingredient_b_id", name="uq_flavor_affinities_pair"),
        CheckConstraint("ingredient_a_id < ingredient_b_id", name="canonical_pair_ordering"),
        CheckConstraint("affinity_score >= 0 AND affinity_score <= 1", name="affinity_score_range"),
    )
