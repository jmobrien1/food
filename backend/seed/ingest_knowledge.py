"""Ingest markdown knowledge docs into pgvector.

Chunks files by heading, embeds with sentence-transformers, and upserts into
the culinary_embeddings table.  Idempotent — skips chunks whose text_content
already exists.

Usage:
    python -m seed.ingest_knowledge [--docs-dir backend/knowledge_docs]
"""

import argparse
import asyncio
import logging
import re
from pathlib import Path

from sqlalchemy import select, func

from app.core.config import settings
from app.core.database import async_session
from app.models.embedding import CulinaryEmbedding

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Markdown chunking
# ---------------------------------------------------------------------------

_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)


def chunk_markdown(text: str, source_name: str) -> list[dict]:
    """Split markdown into chunks at heading boundaries.

    Each chunk keeps the heading as its first line so the embedding captures
    the topic.  Text before the first heading becomes a "preamble" chunk.
    """
    positions = [(m.start(), m.group(2).strip()) for m in _HEADING_RE.finditer(text)]

    if not positions:
        # No headings — treat entire file as one chunk
        return [{"heading": source_name, "body": text.strip()}] if text.strip() else []

    chunks: list[dict] = []

    # Preamble (text before first heading)
    preamble = text[: positions[0][0]].strip()
    if preamble:
        chunks.append({"heading": f"{source_name} — preamble", "body": preamble})

    for idx, (start, heading) in enumerate(positions):
        end = positions[idx + 1][0] if idx + 1 < len(positions) else len(text)
        body = text[start:end].strip()
        if body:
            chunks.append({"heading": heading, "body": body})

    return chunks


# ---------------------------------------------------------------------------
# Embedding helper
# ---------------------------------------------------------------------------


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed with sentence-transformers (CPU, synchronous)."""
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(settings.embedding_model)
    vectors = model.encode(texts, show_progress_bar=True)
    return vectors.tolist()


# ---------------------------------------------------------------------------
# Main ingestion
# ---------------------------------------------------------------------------


async def ingest(docs_dir: Path) -> int:
    md_files = sorted(docs_dir.glob("**/*.md"))
    if not md_files:
        logger.warning("No .md files found in %s", docs_dir)
        return 0

    logger.info("Found %d markdown file(s) in %s", len(md_files), docs_dir)

    all_chunks: list[dict] = []
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        source = md_file.stem
        chunks = chunk_markdown(text, source)
        for chunk in chunks:
            chunk["source_file"] = md_file.name
        all_chunks.extend(chunks)

    logger.info("Produced %d chunks from %d file(s)", len(all_chunks), len(md_files))

    if not all_chunks:
        return 0

    # Check which chunks already exist (idempotent)
    async with async_session() as session:
        existing = set()
        result = await session.execute(
            select(CulinaryEmbedding.text_content).where(
                CulinaryEmbedding.content_type == "knowledge"
            )
        )
        for row in result.scalars():
            existing.add(row)

    new_chunks = [c for c in all_chunks if c["body"] not in existing]
    logger.info(
        "%d new chunks to insert (%d already exist)", len(new_chunks), len(all_chunks) - len(new_chunks)
    )

    if not new_chunks:
        return 0

    # Embed
    texts = [c["body"] for c in new_chunks]
    logger.info("Embedding %d chunks...", len(texts))
    vectors = embed_texts(texts)

    # Insert
    async with async_session() as session:
        async with session.begin():
            for chunk, vec in zip(new_chunks, vectors):
                session.add(
                    CulinaryEmbedding(
                        content_type="knowledge",
                        source_id=0,
                        source_table="knowledge_docs",
                        text_content=chunk["body"],
                        embedding=vec,
                        metadata_={
                            "heading": chunk["heading"],
                            "source_file": chunk["source_file"],
                        },
                    )
                )
        logger.info("Inserted %d knowledge chunks", len(new_chunks))

    return len(new_chunks)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    parser = argparse.ArgumentParser(description="Ingest knowledge docs into pgvector")
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "knowledge_docs",
        help="Directory containing .md files (default: backend/knowledge_docs/)",
    )
    args = parser.parse_args()

    if not args.docs_dir.is_dir():
        logger.error("Docs directory does not exist: %s", args.docs_dir)
        raise SystemExit(1)

    inserted = asyncio.run(ingest(args.docs_dir))
    logger.info("Done — %d new chunks ingested", inserted)


if __name__ == "__main__":
    main()
