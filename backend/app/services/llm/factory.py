from app.core.config import Settings
from app.services.llm.base import LLMService

_instance: LLMService | None = None


def get_llm_service(settings: Settings) -> LLMService:
    global _instance
    if _instance is None:
        if "claude" in settings.llm_model.lower():
            from app.services.llm.anthropic import AnthropicLLMService

            _instance = AnthropicLLMService(settings)
        else:
            from app.services.llm.local import LocalOllamaService

            _instance = LocalOllamaService(settings)
    return _instance
