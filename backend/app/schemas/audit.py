from pydantic import BaseModel, Field


class AuditRequest(BaseModel):
    ingredients: list[str] = Field(..., min_length=1, description="Available ingredients")
    equipment: list[str] = Field(default_factory=list, description="Available equipment")
    time_limit_minutes: int = Field(default=120, ge=15, le=480)
    user_skill: str = Field(
        default="Ambitious Amateur",
        description="Skill level: Home Cook, Ambitious Amateur, Serious Enthusiast",
    )
    guest_count: int = Field(default=2, ge=1, le=20)
    intent: str | None = Field(default=None, description="Optional: what kind of dish?")


class ConstraintFlags(BaseModel):
    can_sous_vide: bool = False
    can_sear_high_heat: bool = False
    can_oven_roast: bool = False
    can_deep_fry: bool = False
    can_smoke: bool = False
    can_torch: bool = False
    has_blender: bool = False
    has_food_processor: bool = False
    has_stand_mixer: bool = False
    max_active_minutes: int = 120
    skill_tier: int = 1  # 1=Home Cook, 2=Ambitious Amateur, 3=Serious Enthusiast
    guest_count: int = 2
