import logging
from collections.abc import AsyncIterator

import anthropic
from pydantic import BaseModel

from app.core.config import Settings

logger = logging.getLogger(__name__)


class AnthropicLLMService:
    def __init__(self, settings: Settings):
        self._client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
        self._model = settings.llm_model
        self._embedder = None
        self._embedding_model_name = settings.embedding_model

    def _get_embedder(self):
        if self._embedder is None:
            from sentence_transformers import SentenceTransformer
            self._embedder = SentenceTransformer(self._embedding_model_name)
        return self._embedder

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel] | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str | BaseModel:
        if response_model is not None:
            return await self._generate_structured(
                system_prompt, user_prompt, response_model, temperature, max_tokens
            )

        message = await self._client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return message.content[0].text

    async def _generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel],
        temperature: float,
        max_tokens: int,
    ) -> BaseModel:
        schema = response_model.model_json_schema()
        tool_name = response_model.__name__

        # Use Claude's tool-use to enforce structured output
        message = await self._client.messages.create(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            tools=[{
                "name": tool_name,
                "description": f"Return the result as a {tool_name} object",
                "input_schema": schema,
            }],
            tool_choice={"type": "tool", "name": tool_name},
        )

        for block in message.content:
            if block.type == "tool_use":
                return response_model.model_validate(block.input)

        raise ValueError(f"No tool_use block in response for {tool_name}")

    async def generate_stream(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> AsyncIterator[str]:
        async with self._client.messages.stream(
            model=self._model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        ) as stream:
            async for text in stream.text_stream:
                yield text

    async def embed(self, texts: list[str]) -> list[list[float]]:
        embedder = self._get_embedder()
        embeddings = embedder.encode(texts, show_progress_bar=False)
        return embeddings.tolist()

    async def check_connectivity(self) -> bool:
        try:
            await self._client.messages.create(
                model=self._model,
                max_tokens=10,
                messages=[{"role": "user", "content": "ping"}],
            )
            return True
        except Exception:
            return False
