from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.ingredients import router as ingredients_router
from app.api.v1.plans import router as plans_router
from app.api.v1.substitutions import router as substitutions_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health_router)
api_router.include_router(plans_router)
api_router.include_router(ingredients_router)
api_router.include_router(substitutions_router)
