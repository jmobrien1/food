from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.config import settings
from app.models.base import Base


class CulinaryEmbedding(Base):
    __tablename__ = "culinary_embeddings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content_type: Mapped[str] = mapped_column(String(50), nullable=False)
    source_id: Mapped[int] = mapped_column(Integer, nullable=False)
    source_table: Mapped[str] = mapped_column(String(100), nullable=False)
    text_content: Mapped[str] = mapped_column(Text, nullable=False)
    embedding: Mapped[Any] = mapped_column(Vector(settings.embedding_dim), nullable=False)
    metadata_: Mapped[dict | None] = mapped_column("metadata", JSONB)
