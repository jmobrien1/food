"""Unit tests for the LLM factory — routing + singleton behaviour."""

from unittest.mock import patch

import pytest

from app.core.config import Settings


@pytest.fixture(autouse=True)
def _reset_singleton():
    """Reset the factory singleton before each test."""
    import app.services.llm.factory as factory_mod

    factory_mod._instance = None
    yield
    factory_mod._instance = None


def _make_settings(**overrides) -> Settings:
    defaults = {
        "database_url": "postgresql+asyncpg://x:x@localhost/x",
        "anthropic_api_key": "sk-ant-test",
        "ollama_base_url": "http://localhost:11434",
        "llm_model": "qwen2.5",
    }
    defaults.update(overrides)
    return Settings(**defaults)


def test_factory_returns_ollama_for_non_claude_model():
    from app.services.llm.factory import get_llm_service
    from app.services.llm.local import LocalOllamaService

    svc = get_llm_service(_make_settings(llm_model="qwen2.5"))
    assert isinstance(svc, LocalOllamaService)


def test_factory_returns_ollama_for_llama_model():
    from app.services.llm.factory import get_llm_service
    from app.services.llm.local import LocalOllamaService

    svc = get_llm_service(_make_settings(llm_model="llama3.1"))
    assert isinstance(svc, LocalOllamaService)


def test_factory_returns_anthropic_for_claude_model():
    from app.services.llm.factory import get_llm_service
    from app.services.llm.anthropic import AnthropicLLMService

    svc = get_llm_service(_make_settings(llm_model="claude-sonnet-4-6"))
    assert isinstance(svc, AnthropicLLMService)


def test_factory_returns_anthropic_for_claude_uppercase():
    from app.services.llm.factory import get_llm_service
    from app.services.llm.anthropic import AnthropicLLMService

    svc = get_llm_service(_make_settings(llm_model="Claude-3-Opus"))
    assert isinstance(svc, AnthropicLLMService)


def test_factory_is_singleton():
    from app.services.llm.factory import get_llm_service

    settings = _make_settings(llm_model="qwen2.5")
    svc1 = get_llm_service(settings)
    svc2 = get_llm_service(settings)
    assert svc1 is svc2
