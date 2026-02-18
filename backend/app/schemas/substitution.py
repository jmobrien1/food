from pydantic import BaseModel, Field


class SubstitutionRequest(BaseModel):
    ingredient_name: str
    available_ingredients: list[str] = Field(default_factory=list)
    dish_context: str | None = None


class SubstitutionSuggestion(BaseModel):
    original: str
    substitute: str
    jaccard_score: float
    rationale: str
    adjustment_notes: str | None = None


class SubstitutionResponse(BaseModel):
    suggestions: list[SubstitutionSuggestion]
