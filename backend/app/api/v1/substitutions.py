from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.ingredient import Ingredient
from app.schemas.substitution import SubstitutionRequest, SubstitutionResponse, SubstitutionSuggestion
from app.services.flavor_graph import find_substitutes

router = APIRouter(prefix="/substitutions", tags=["substitutions"])


@router.post("/suggest", response_model=SubstitutionResponse)
async def suggest_substitutions(
    body: SubstitutionRequest,
    session: AsyncSession = Depends(get_session),
):
    # Find the ingredient to substitute
    stmt = select(Ingredient).where(func.lower(Ingredient.name) == body.ingredient_name.lower())
    result = await session.execute(stmt)
    ingredient = result.scalar_one_or_none()

    if not ingredient:
        return SubstitutionResponse(suggestions=[])

    # Find candidate IDs if available_ingredients is provided
    candidate_ids = None
    if body.available_ingredients:
        stmt = select(Ingredient.id).where(
            func.lower(Ingredient.name).in_([n.lower() for n in body.available_ingredients])
        )
        result = await session.execute(stmt)
        candidate_ids = [row[0] for row in result.all()]

    substitutes = await find_substitutes(
        session, ingredient.id, candidate_ids=candidate_ids, top_k=5
    )

    suggestions = [
        SubstitutionSuggestion(
            original=body.ingredient_name,
            substitute=sub["ingredient_name"],
            jaccard_score=sub["jaccard_score"],
            rationale=f"Shares {int(sub['jaccard_score'] * 100)}% flavor profile overlap",
        )
        for sub in substitutes
        if sub["jaccard_score"] > 0
    ]

    return SubstitutionResponse(suggestions=suggestions)
