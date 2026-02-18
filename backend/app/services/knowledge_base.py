"""Semantic search over culinary knowledge using pgvector."""

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.embedding import CulinaryEmbedding
from app.services.llm.base import LLMService


async def search_knowledge(
    session: AsyncSession,
    llm_service: LLMService,
    query: str,
    content_type: str | None = None,
    top_k: int = 5,
) -> list[dict]:
    """Semantic search over culinary embeddings."""
    # Generate query embedding
    embeddings = await llm_service.embed([query])
    query_embedding = embeddings[0]

    # Build query with cosine similarity
    filters = []
    params = {"embedding": str(query_embedding), "limit": top_k}

    if content_type:
        filters.append("content_type = :content_type")
        params["content_type"] = content_type

    where_clause = f"WHERE {' AND '.join(filters)}" if filters else ""

    sql = text(f"""
        SELECT id, content_type, source_table, text_content, metadata,
               1 - (embedding <=> :embedding::vector) AS similarity
        FROM culinary_embeddings
        {where_clause}
        ORDER BY embedding <=> :embedding::vector
        LIMIT :limit
    """)

    result = await session.execute(sql, params)
    return [
        {
            "id": row.id,
            "content_type": row.content_type,
            "source_table": row.source_table,
            "text_content": row.text_content,
            "metadata": row.metadata,
            "similarity": round(float(row.similarity), 4),
        }
        for row in result.all()
    ]


async def index_content(
    session: AsyncSession,
    llm_service: LLMService,
    content_type: str,
    source_id: int,
    source_table: str,
    text_content: str,
    metadata: dict | None = None,
):
    """Index a piece of culinary content for semantic search."""
    embeddings = await llm_service.embed([text_content])

    embedding_record = CulinaryEmbedding(
        content_type=content_type,
        source_id=source_id,
        source_table=source_table,
        text_content=text_content,
        embedding=embeddings[0],
        metadata_=metadata,
    )
    session.add(embedding_record)
    await session.flush()
