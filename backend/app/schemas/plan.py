from pydantic import BaseModel, Field


class PlanIngredient(BaseModel):
    name: str
    amount_grams: float
    original_amount: str
    is_substitute: bool = False
    substitute_for: str | None = None
    scaling_notes: str | None = None


class TimelineTask(BaseModel):
    step: int
    description: str
    duration_minutes: int
    is_active: bool = True
    technique: str | None = None
    pro_tip: str | None = None


class TimelinePhase(BaseModel):
    phase: str  # "Day Before", "Hour Before", "Active Cooking"
    tasks: list[TimelineTask]


class ChefSecret(BaseModel):
    category: str  # "Finishing", "Plating", "Flavor Boost", "Timing"
    tip: str
    why_it_works: str | None = None


class ExecutionPlan(BaseModel):
    dish_name: str
    dish_description: str
    serves: int
    total_time_minutes: int
    active_time_minutes: int
    difficulty: str
    ingredients: list[PlanIngredient]
    substitution_notes: list[str] = []
    timeline: list[TimelinePhase]
    chefs_secrets: list[ChefSecret] = []


class PlanGenerateResponse(BaseModel):
    id: str
    plan: ExecutionPlan


class PlanGetResponse(BaseModel):
    id: str
    plan: ExecutionPlan
    model_used: str
    latency_ms: int

    model_config = {"from_attributes": True}


class PlanGenerateRequest(BaseModel):
    ingredients: list[str] = Field(default_factory=list)
    equipment: list[str] = Field(default_factory=list)
    time_limit_minutes: int = Field(default=120, ge=0, le=2880, description="0 means unlimited")
    user_skill: str = Field(default="Ambitious Amateur")
    guest_count: int = Field(default=2, ge=1, le=20)
    intent: str | None = None
