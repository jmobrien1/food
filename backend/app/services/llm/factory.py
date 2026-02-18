from app.core.config import Settings
from app.services.llm.anthropic import AnthropicLLMService
from app.services.llm.base import LLMService

_instance: LLMService | None = None


def get_llm_service(settings: Settings) -> LLMService:
    global _instance
    if _instance is None:
        _instance = AnthropicLLMService(settings)
    return _instance
