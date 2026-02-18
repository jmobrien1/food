"""Unit tests for LocalOllamaService — generation, structured output, embedding, health."""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest
from pydantic import BaseModel

from app.core.config import Settings
from app.services.llm.local import LocalOllamaService, _CODE_FENCE_RE


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


class SampleModel(BaseModel):
    name: str
    score: float


def _make_service(**overrides) -> LocalOllamaService:
    defaults = {
        "database_url": "postgresql+asyncpg://x:x@localhost/x",
        "ollama_base_url": "http://localhost:11434",
        "llm_model": "qwen2.5",
    }
    defaults.update(overrides)
    return LocalOllamaService(Settings(**defaults))


# ---------------------------------------------------------------------------
# generate() — plain text
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_generate_plain_text():
    svc = _make_service()

    mock_response = MagicMock()
    mock_response.json.return_value = {"response": "Hello from Ollama"}
    mock_response.raise_for_status = MagicMock()

    with patch("app.services.llm.local.httpx.AsyncClient") as MockClient:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        MockClient.return_value = mock_client

        result = await svc.generate("You are helpful.", "Say hello")

    assert result == "Hello from Ollama"
    mock_client.post.assert_called_once()
    call_args = mock_client.post.call_args
    assert call_args[0][0] == "http://localhost:11434/api/generate"
    payload = call_args[1]["json"]
    assert payload["model"] == "qwen2.5"
    assert payload["stream"] is False
    assert "format" not in payload  # no JSON format for plain text


# ---------------------------------------------------------------------------
# generate() — structured output
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_generate_structured_output():
    svc = _make_service()

    raw_json = json.dumps({"name": "test", "score": 0.95})
    mock_response = MagicMock()
    mock_response.json.return_value = {"response": raw_json}
    mock_response.raise_for_status = MagicMock()

    with patch("app.services.llm.local.httpx.AsyncClient") as MockClient:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        MockClient.return_value = mock_client

        result = await svc.generate("sys", "prompt", response_model=SampleModel)

    assert isinstance(result, SampleModel)
    assert result.name == "test"
    assert result.score == 0.95

    # Verify JSON format was requested
    payload = mock_client.post.call_args[1]["json"]
    assert payload["format"] == "json"


# ---------------------------------------------------------------------------
# generate() — handles markdown code fences
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_generate_structured_handles_code_fences():
    svc = _make_service()

    fenced = '```json\n{"name": "fenced", "score": 1.0}\n```'
    mock_response = MagicMock()
    mock_response.json.return_value = {"response": fenced}
    mock_response.raise_for_status = MagicMock()

    with patch("app.services.llm.local.httpx.AsyncClient") as MockClient:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        MockClient.return_value = mock_client

        result = await svc.generate("sys", "prompt", response_model=SampleModel)

    assert isinstance(result, SampleModel)
    assert result.name == "fenced"
    assert result.score == 1.0


@pytest.mark.asyncio
async def test_generate_structured_handles_bare_fences():
    """Code fences without the 'json' language tag."""
    svc = _make_service()

    fenced = '```\n{"name": "bare", "score": 0.5}\n```'
    mock_response = MagicMock()
    mock_response.json.return_value = {"response": fenced}
    mock_response.raise_for_status = MagicMock()

    with patch("app.services.llm.local.httpx.AsyncClient") as MockClient:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        MockClient.return_value = mock_client

        result = await svc.generate("sys", "prompt", response_model=SampleModel)

    assert isinstance(result, SampleModel)
    assert result.name == "bare"


# ---------------------------------------------------------------------------
# check_connectivity
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_check_connectivity_success():
    svc = _make_service()

    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch("app.services.llm.local.httpx.AsyncClient") as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        MockClient.return_value = mock_client

        assert await svc.check_connectivity() is True

    mock_client.get.assert_called_once_with("http://localhost:11434/api/tags")


@pytest.mark.asyncio
async def test_check_connectivity_failure():
    svc = _make_service()

    with patch("app.services.llm.local.httpx.AsyncClient") as MockClient:
        mock_client = AsyncMock()
        mock_client.get.side_effect = httpx.ConnectError("refused")
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        MockClient.return_value = mock_client

        assert await svc.check_connectivity() is False


# ---------------------------------------------------------------------------
# embed
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_embed():
    svc = _make_service()

    fake_embeddings = MagicMock()
    fake_embeddings.tolist.return_value = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]

    mock_model = MagicMock()
    mock_model.encode.return_value = fake_embeddings

    with patch.object(svc, "_get_embedder", return_value=mock_model):
        result = await svc.embed(["hello", "world"])

    assert result == [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    mock_model.encode.assert_called_once_with(["hello", "world"], show_progress_bar=False)


# ---------------------------------------------------------------------------
# _CODE_FENCE_RE regex unit tests
# ---------------------------------------------------------------------------


def test_code_fence_regex_json_tag():
    text = '```json\n{"key": "value"}\n```'
    match = _CODE_FENCE_RE.search(text)
    assert match is not None
    assert '{"key": "value"}' in match.group(1)


def test_code_fence_regex_no_tag():
    text = '```\n{"key": "value"}\n```'
    match = _CODE_FENCE_RE.search(text)
    assert match is not None
    assert '{"key": "value"}' in match.group(1)


def test_code_fence_regex_no_fences():
    text = '{"key": "value"}'
    match = _CODE_FENCE_RE.search(text)
    assert match is None
