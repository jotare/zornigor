import sqlalchemy as sa

metadata = sa.MetaData()


projects = sa.Table(
    "projects",
    metadata,
    sa.Column("slug", sa.String, nullable=False, primary_key=True),
    sa.Column("description", sa.String, nullable=True),
    sa.Column("created", sa.DateTime, default=sa.func.now()),
)

states = sa.Table(
    "states",
    metadata,
    sa.Column("slug", sa.String, primary_key=True),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("description", sa.String, server_default=""),
    sa.Column("color", sa.String(6), server_default="000000", comment="Hex RGB color"),
    sa.Column("project", sa.String, sa.ForeignKey("projects.slug"), primary_key=True),
)

stories = sa.Table(
    "stories",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String, nullable=False),
    sa.Column("description", sa.String, default=""),
    sa.Column("created", sa.DateTime, default=sa.func.now()),
    sa.Column("modified", sa.DateTime, default=sa.func.now()),
    sa.Column("project", sa.String, sa.ForeignKey("projects.slug"), primary_key=True),
    sa.Column("state", sa.String, sa.ForeignKey("states.slug")),
)