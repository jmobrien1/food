from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://chefdecuisine:changeme@db:5432/chefdecuisine"

    # Anthropic (used when llm_model contains "claude")
    anthropic_api_key: str = ""

    # Ollama (used for all other models)
    ollama_base_url: str = "http://host.docker.internal:11434"

    # LLM
    llm_model: str = "qwen2.5"

    # Server
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    cors_origins: list[str] = ["http://localhost:3004", "http://10.0.0.5:3004"]

    # Embedding
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dim: int = 384

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
