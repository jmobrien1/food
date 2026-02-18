"""Local Ollama LLM service — drop-in replacement for AnthropicLLMService."""

import json
import logging
import re
from collections.abc import AsyncIterator

import httpx
from pydantic import BaseModel

from app.core.config import Settings

logger = logging.getLogger(__name__)

# Regex to strip markdown code fences from LLM output
_CODE_FENCE_RE = re.compile(r"```(?:json)?\s*\n?(.*?)\n?\s*```", re.DOTALL)


class LocalOllamaService:
    """LLMService implementation backed by a local Ollama instance."""

    def __init__(self, settings: Settings):
        self._base_url = settings.ollama_base_url.rstrip("/")
        self._model = settings.llm_model
        self._embedder = None
        self._embedding_model_name = settings.embedding_model

    # ------------------------------------------------------------------
    # Embedding (sentence-transformers, lazy-loaded)
    # ------------------------------------------------------------------

    def _get_embedder(self):
        if self._embedder is None:
            from sentence_transformers import SentenceTransformer

            self._embedder = SentenceTransformer(self._embedding_model_name)
        return self._embedder

    # ------------------------------------------------------------------
    # Generation
    # ------------------------------------------------------------------

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel] | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str | BaseModel:
        payload = {
            "model": self._model,
            "prompt": user_prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }

        if response_model is not None:
            payload["format"] = "json"
            payload["system"] += (
                f"\n\nRespond with valid JSON matching this schema: "
                f"{json.dumps(response_model.model_json_schema())}"
            )

        async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
            resp = await client.post(f"{self._base_url}/api/generate", json=payload)
            resp.raise_for_status()

        text: str = resp.json()["response"]

        if response_model is None:
            return text

        return self._parse_structured(text, response_model)

    # ------------------------------------------------------------------
    # Streaming
    # ------------------------------------------------------------------

    async def generate_stream(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> AsyncIterator[str]:
        payload = {
            "model": self._model,
            "prompt": user_prompt,
            "system": system_prompt,
            "stream": True,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens,
            },
        }

        async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
            async with client.stream(
                "POST", f"{self._base_url}/api/generate", json=payload
            ) as resp:
                resp.raise_for_status()
                async for line in resp.aiter_lines():
                    if not line:
                        continue
                    chunk = json.loads(line)
                    if token := chunk.get("response", ""):
                        yield token
                    if chunk.get("done"):
                        break

    # ------------------------------------------------------------------
    # Embedding
    # ------------------------------------------------------------------

    async def embed(self, texts: list[str]) -> list[list[float]]:
        embedder = self._get_embedder()
        embeddings = embedder.encode(texts, show_progress_bar=False)
        return embeddings.tolist()

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------

    async def check_connectivity(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(5.0)) as client:
                resp = await client.get(f"{self._base_url}/api/tags")
                return resp.status_code == 200
        except Exception:
            logger.warning("Ollama connectivity check failed", exc_info=True)
            return False

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_structured(text: str, response_model: type[BaseModel]) -> BaseModel:
        """Parse JSON from LLM output, stripping markdown code fences if present."""
        cleaned = text.strip()

        # Strip markdown code fences (```json ... ``` or ``` ... ```)
        match = _CODE_FENCE_RE.search(cleaned)
        if match:
            cleaned = match.group(1).strip()

        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError as exc:
            logger.error("Failed to parse structured output: %s\nRaw text: %s", exc, text)
            raise ValueError(f"LLM returned invalid JSON: {exc}") from exc

        return response_model.model_validate(data)
