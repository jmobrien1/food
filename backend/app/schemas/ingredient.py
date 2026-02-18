from pydantic import BaseModel


class FlavorProfileOut(BaseModel):
    descriptor: str
    intensity: float


class IngredientOut(BaseModel):
    id: int
    name: str
    category: str
    subcategory: str | None = None
    is_potent: bool = False
    scaling_exponent: float = 1.0
    safety_ceiling: float | None = None
    flavor_profiles: list[FlavorProfileOut] = []

    model_config = {"from_attributes": True}


class IngredientSearchResult(BaseModel):
    id: int
    name: str
    category: str

    model_config = {"from_attributes": True}


class AffinityOut(BaseModel):
    ingredient_name: str
    affinity_score: float
    source: str | None = None
