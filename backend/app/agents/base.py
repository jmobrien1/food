"""Shared context passed through the 4-agent pipeline."""

from dataclasses import dataclass, field
from typing import Any

from app.schemas.audit import AuditRequest, ConstraintFlags
from app.schemas.plan import (
    ChefSecret,
    ExecutionPlan,
    PlanIngredient,
    TimelinePhase,
)


@dataclass
class AgentTrace:
    agent_name: str
    input_summary: str
    output_summary: str
    latency_ms: int = 0
    error: str | None = None


@dataclass
class AgentContext:
    # Input
    audit_request: AuditRequest

    # Phase 1: Auditor output
    constraints: ConstraintFlags | None = None
    flags: list[str] = field(default_factory=list)

    # Phase 2: Translator output
    dish_concept: str = ""
    dish_name: str = ""
    dish_description: str = ""
    difficulty: str = "Intermediate"
    ingredients_list: list[PlanIngredient] = field(default_factory=list)
    substitution_notes: list[str] = field(default_factory=list)

    # Phase 3: Scheduler output
    timeline: list[TimelinePhase] = field(default_factory=list)
    total_time_minutes: int = 0
    active_time_minutes: int = 0

    # Phase 4: Executive Chef output
    chefs_secrets: list[ChefSecret] = field(default_factory=list)

    # Tracing
    trace: list[AgentTrace] = field(default_factory=list)

    def to_plan(self) -> ExecutionPlan:
        return ExecutionPlan(
            dish_name=self.dish_name,
            dish_description=self.dish_description,
            serves=self.audit_request.guest_count,
            total_time_minutes=self.total_time_minutes,
            active_time_minutes=self.active_time_minutes,
            difficulty=self.difficulty,
            ingredients=self.ingredients_list,
            substitution_notes=self.substitution_notes,
            timeline=self.timeline,
            chefs_secrets=self.chefs_secrets,
        )
