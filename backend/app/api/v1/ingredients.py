from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.database import get_session
from app.models.ingredient import Ingredient
from app.schemas.ingredient import AffinityOut, IngredientOut, IngredientSearchResult
from app.services.flavor_graph import get_affinities_for_ingredient

router = APIRouter(prefix="/ingredients", tags=["ingredients"])


@router.get("", response_model=list[IngredientSearchResult])
async def search_ingredients(
    q: str = Query(default="", description="Search query"),
    category: str | None = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100),
    session: AsyncSession = Depends(get_session),
):
    stmt = select(Ingredient)
    if q:
        stmt = stmt.where(Ingredient.name.ilike(f"%{q}%"))
    if category:
        stmt = stmt.where(func.lower(Ingredient.category) == category.lower())
    stmt = stmt.order_by(Ingredient.name).limit(limit)

    result = await session.execute(stmt)
    return result.scalars().all()


@router.get("/{ingredient_id}", response_model=IngredientOut)
async def get_ingredient(
    ingredient_id: int,
    session: AsyncSession = Depends(get_session),
):
    stmt = (
        select(Ingredient)
        .options(selectinload(Ingredient.flavor_profiles))
        .where(Ingredient.id == ingredient_id)
    )
    result = await session.execute(stmt)
    ingredient = result.scalar_one_or_none()
    if not ingredient:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient


@router.get("/{ingredient_id}/affinities", response_model=list[AffinityOut])
async def get_ingredient_affinities(
    ingredient_id: int,
    min_score: float = Query(default=0.0, ge=0, le=1),
    limit: int = Query(default=20, ge=1, le=50),
    session: AsyncSession = Depends(get_session),
):
    return await get_affinities_for_ingredient(session, ingredient_id, min_score, limit)
