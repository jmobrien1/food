"""Unit tests for the auditor agent (deterministic constraint mapping)."""

import pytest
from app.agents.base import AgentContext
from app.schemas.audit import AuditRequest


@pytest.fixture
def basic_context():
    return AgentContext(
        audit_request=AuditRequest(
            ingredients=["chicken", "lemon"],
            equipment=["cast iron skillet", "oven"],
            time_limit_minutes=90,
            user_skill="Ambitious Amateur",
            guest_count=4,
        )
    )


def test_skill_tier_mapping():
    from app.agents.auditor import SKILL_MAP
    assert SKILL_MAP["Home Cook"] == 1
    assert SKILL_MAP["Ambitious Amateur"] == 2
    assert SKILL_MAP["Serious Enthusiast"] == 3


def test_capability_rules_coverage():
    from app.agents.auditor import CAPABILITY_RULES
    # Ensure key equipment is covered
    assert "cast iron" in CAPABILITY_RULES
    assert "oven" in CAPABILITY_RULES
    assert "blender" in CAPABILITY_RULES
    assert "sous vide" in CAPABILITY_RULES
