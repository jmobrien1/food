"""Test fixtures: MockLLM, test DB session, common fixtures."""

import asyncio
from typing import Any

import pytest
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.models.base import Base
from app.schemas.plan import (
    ChefSecret,
    ExecutionPlan,
    PlanIngredient,
    TimelinePhase,
    TimelineTask,
)


class MockLLMService:
    """Mock LLM that returns deterministic structured outputs."""

    _model = "mock-model"

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel] | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str | BaseModel:
        if response_model is None:
            return "Mock LLM response"

        # Return mock data based on the response model
        model_name = response_model.__name__

        if model_name == "TranslatorOutput":
            from app.agents.translator import TranslatorOutput
            return TranslatorOutput(
                dish_name="Pan-Seared Lemon Thyme Chicken",
                dish_description="Crispy-skinned chicken with bright lemon and fragrant thyme.",
                difficulty="Intermediate",
                ingredients=[
                    PlanIngredient(name="chicken breast", amount_grams=350, original_amount="2 medium breasts"),
                    PlanIngredient(name="lemon", amount_grams=60, original_amount="1 medium lemon"),
                    PlanIngredient(name="thyme", amount_grams=5, original_amount="4-5 sprigs"),
                    PlanIngredient(name="butter", amount_grams=30, original_amount="2 tablespoons"),
                ],
                substitution_notes=[],
            )

        if model_name == "SchedulerOutput":
            from app.agents.scheduler import SchedulerOutput
            return SchedulerOutput(
                timeline=[
                    TimelinePhase(
                        phase="Active Cooking",
                        tasks=[
                            TimelineTask(step=1, description="Season chicken", duration_minutes=5, is_active=True),
                            TimelineTask(step=2, description="Sear chicken", duration_minutes=8, is_active=True),
                            TimelineTask(step=3, description="Rest chicken", duration_minutes=5, is_active=False),
                        ],
                    )
                ],
                total_time_minutes=18,
                active_time_minutes=13,
            )

        if model_name == "ExecChefOutput":
            from app.agents.executive_chef import ExecChefOutput
            return ExecChefOutput(
                chefs_secrets=[
                    ChefSecret(
                        category="Finishing",
                        tip="Add a squeeze of lemon and flaky salt just before serving.",
                        why_it_works="Acid brightness lifts all the flavors.",
                    )
                ],
                additional_tasks=[],
                review_notes=[],
            )

        # Fallback: try to construct with minimal data
        return response_model.model_validate({})

    async def generate_stream(self, system_prompt, user_prompt, **kwargs):
        yield "Mock stream response"

    async def embed(self, texts: list[str]) -> list[list[float]]:
        return [[0.0] * 384 for _ in texts]

    async def check_connectivity(self) -> bool:
        return True


@pytest.fixture
def mock_llm():
    return MockLLMService()


@pytest.fixture
def sample_audit_request():
    from app.schemas.audit import AuditRequest
    return AuditRequest(
        ingredients=["chicken breast", "lemon", "thyme", "butter"],
        equipment=["cast iron skillet", "oven"],
        time_limit_minutes=90,
        user_skill="Ambitious Amateur",
        guest_count=4,
    )
