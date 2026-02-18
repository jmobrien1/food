from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://chefdecuisine:changeme@db:5432/chefdecuisine"

    # Anthropic
    anthropic_api_key: str = ""
    llm_model: str = "claude-sonnet-4-6-20250514"

    # Server
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    cors_origins: list[str] = ["http://localhost:3001", "http://10.0.0.5:3001"]

    # Embedding
    embedding_model: str = "all-MiniLM-L6-v2"
    embedding_dim: int = 384

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
