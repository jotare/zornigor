"""Create initial tables

Revision ID: 63c81cc708cd
Revises:
Create Date: 2023-04-25 21:04:14.341476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c81cc708cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("slug", sa.String, nullable=False, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("created", sa.DateTime, default=sa.func.now(), nullable=False),
        sa.Column("modified", sa.DateTime, default=sa.func.now(), nullable=False),
        sa.Column("last_story_id", sa.Integer, nullable=False, server_default=sa.text("0")),
    )

    op.create_table(
        "states",
        sa.Column("slug", sa.String, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, server_default=""),
        sa.Column("color", sa.String(6), server_default="000000", comment="Hex RGB color"),
        sa.Column("project", sa.String, primary_key=True),

        sa.ForeignKeyConstraint(["project"], ["projects.slug"]),
    )

    op.create_table(
        "stories",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("description", sa.String, default=""),
        sa.Column("created", sa.DateTime, default=sa.func.now()),
        sa.Column("modified", sa.DateTime, default=sa.func.now()),
        sa.Column("project", sa.String, primary_key=True),
        sa.Column("state", sa.String),

        sa.ForeignKeyConstraint(["project"], ["projects.slug"]),
        sa.ForeignKeyConstraint(["project", "state"], ["states.project", "states.slug"]),
    )


def downgrade() -> None:
    op.drop_table("stories")
    op.drop_table("states")
    op.drop_table("projects")
