"""Flavor affinity queries and Jaccard similarity for substitutions.

Replaces Neo4j graph with SQL queries against PostgreSQL.
"""

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.flavor_affinity import FlavorAffinity
from app.models.flavor_profile import FlavorProfile
from app.models.ingredient import Ingredient


async def get_affinities_for_ingredient(
    session: AsyncSession,
    ingredient_id: int,
    min_score: float = 0.0,
    limit: int = 20,
) -> list[dict]:
    """Get top flavor affinities for an ingredient, sorted by score."""
    # Query both directions of the pair
    stmt = (
        select(
            FlavorAffinity.affinity_score,
            FlavorAffinity.source,
            Ingredient.name,
        )
        .join(
            Ingredient,
            or_(
                (FlavorAffinity.ingredient_a_id == ingredient_id)
                & (Ingredient.id == FlavorAffinity.ingredient_b_id),
                (FlavorAffinity.ingredient_b_id == ingredient_id)
                & (Ingredient.id == FlavorAffinity.ingredient_a_id),
            ),
        )
        .where(
            or_(
                FlavorAffinity.ingredient_a_id == ingredient_id,
                FlavorAffinity.ingredient_b_id == ingredient_id,
            )
        )
        .where(FlavorAffinity.affinity_score >= min_score)
        .order_by(FlavorAffinity.affinity_score.desc())
        .limit(limit)
    )
    result = await session.execute(stmt)
    return [
        {"ingredient_name": row.name, "affinity_score": row.affinity_score, "source": row.source}
        for row in result.all()
    ]


async def get_flavor_descriptors(
    session: AsyncSession, ingredient_id: int
) -> set[str]:
    """Get the set of flavor descriptors for an ingredient."""
    stmt = select(FlavorProfile.descriptor).where(
        FlavorProfile.ingredient_id == ingredient_id
    )
    result = await session.execute(stmt)
    return {row[0] for row in result.all()}


async def jaccard_similarity(
    session: AsyncSession,
    ingredient_a_id: int,
    ingredient_b_id: int,
) -> float:
    """Compute Jaccard similarity between two ingredients based on flavor descriptors."""
    set_a = await get_flavor_descriptors(session, ingredient_a_id)
    set_b = await get_flavor_descriptors(session, ingredient_b_id)

    if not set_a and not set_b:
        return 0.0

    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union) if union else 0.0


async def find_substitutes(
    session: AsyncSession,
    ingredient_id: int,
    candidate_ids: list[int] | None = None,
    top_k: int = 5,
) -> list[dict]:
    """Find best substitutes for an ingredient using Jaccard similarity.

    If candidate_ids is provided, only consider those ingredients.
    Otherwise, considers all ingredients in the same category.
    """
    # Get the target ingredient
    target = await session.get(Ingredient, ingredient_id)
    if not target:
        return []

    if candidate_ids:
        stmt = select(Ingredient).where(Ingredient.id.in_(candidate_ids))
    else:
        stmt = select(Ingredient).where(
            Ingredient.category == target.category,
            Ingredient.id != ingredient_id,
        )

    result = await session.execute(stmt)
    candidates = result.scalars().all()

    scores = []
    for candidate in candidates:
        score = await jaccard_similarity(session, ingredient_id, candidate.id)
        scores.append({
            "ingredient_id": candidate.id,
            "ingredient_name": candidate.name,
            "jaccard_score": round(score, 3),
        })

    scores.sort(key=lambda x: x["jaccard_score"], reverse=True)
    return scores[:top_k]
