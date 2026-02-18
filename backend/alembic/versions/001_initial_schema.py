"""initial schema

Revision ID: 001
Revises:
Create Date: 2026-02-18
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from pgvector.sqlalchemy import Vector

# revision identifiers
revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # --- ingredients ---
    op.create_table(
        "ingredients",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(200), nullable=False, unique=True),
        sa.Column("category", sa.String(100), nullable=False),
        sa.Column("subcategory", sa.String(100), nullable=True),
        sa.Column("is_potent", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("scaling_exponent", sa.Float(), server_default=sa.text("1.0")),
        sa.Column("safety_ceiling", sa.Float(), nullable=True),
    )
    op.execute(
        "CREATE INDEX ix_ingredients_name_trgm ON ingredients USING gin (name gin_trgm_ops)"
    )

    # --- flavor_profiles ---
    op.create_table(
        "flavor_profiles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "ingredient_id",
            sa.Integer(),
            sa.ForeignKey("ingredients.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("descriptor", sa.String(100), nullable=False),
        sa.Column("intensity", sa.Float(), nullable=False),
        sa.UniqueConstraint(
            "ingredient_id", "descriptor", name="uq_flavor_profiles_ingredient_descriptor"
        ),
    )

    # --- flavor_affinities ---
    op.create_table(
        "flavor_affinities",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "ingredient_a_id",
            sa.Integer(),
            sa.ForeignKey("ingredients.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "ingredient_b_id",
            sa.Integer(),
            sa.ForeignKey("ingredients.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("affinity_score", sa.Float(), nullable=False),
        sa.Column("source", sa.String(200), nullable=True),
        sa.UniqueConstraint(
            "ingredient_a_id", "ingredient_b_id", name="uq_flavor_affinities_pair"
        ),
        sa.CheckConstraint(
            "ingredient_a_id < ingredient_b_id", name="canonical_pair_ordering"
        ),
        sa.CheckConstraint(
            "affinity_score >= 0 AND affinity_score <= 1", name="affinity_score_range"
        ),
    )

    # --- equipment ---
    op.create_table(
        "equipment",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(200), nullable=False, unique=True),
        sa.Column("category", sa.String(100), nullable=False),
        sa.Column("is_professional", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("capabilities", postgresql.ARRAY(sa.String()), server_default="{}"),
        sa.Column("home_alt", sa.String(200), nullable=True),
    )

    # --- techniques ---
    op.create_table(
        "techniques",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(200), nullable=False, unique=True),
        sa.Column("category", sa.String(100), nullable=False),
        sa.Column("min_skill_level", sa.String(50), nullable=False),
        sa.Column("required_equipment", sa.String(200), nullable=True),
        sa.Column("time_minutes", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("pro_tip", sa.Text(), nullable=True),
        sa.Column(
            "fallback_technique_id",
            sa.Integer(),
            sa.ForeignKey("techniques.id"),
            nullable=True,
        ),
    )

    # --- culinary_embeddings ---
    op.create_table(
        "culinary_embeddings",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("content_type", sa.String(50), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("source_table", sa.String(100), nullable=False),
        sa.Column("text_content", sa.Text(), nullable=False),
        sa.Column("embedding", Vector(384), nullable=False),
        sa.Column("metadata", postgresql.JSONB(), nullable=True),
    )
    # NOTE: IVFFlat index should be created after data is loaded:
    # CREATE INDEX ix_culinary_embeddings_embedding
    #   ON culinary_embeddings USING ivfflat (embedding vector_cosine_ops)
    #   WITH (lists = 100);

    # --- plan_history ---
    op.create_table(
        "plan_history",
        sa.Column(
            "id", postgresql.UUID(as_uuid=True), primary_key=True
        ),
        sa.Column("audit_request", postgresql.JSONB(), nullable=False),
        sa.Column("constraints", postgresql.JSONB(), nullable=False),
        sa.Column("execution_plan", postgresql.JSONB(), nullable=False),
        sa.Column("agent_traces", postgresql.JSONB(), nullable=True),
        sa.Column("model_used", sa.String(100), nullable=False),
        sa.Column("latency_ms", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
        ),
    )


def downgrade() -> None:
    op.drop_table("plan_history")
    op.drop_table("culinary_embeddings")
    op.drop_table("techniques")
    op.drop_table("equipment")
    op.drop_table("flavor_affinities")
    op.drop_table("flavor_profiles")
    op.drop_table("ingredients")
