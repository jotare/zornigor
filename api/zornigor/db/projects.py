from typing import List, Optional

from sqlalchemy import insert, select

from zornigor.db.models import Project
from zornigor.db.tables import projects
from zornigor.db.utility import get_database


async def create_project(project: Project):
    db = get_database(strict=True)
    stmt = insert(projects).values(**project.dict())
    await db.execute(stmt)


async def get_project(slug: str) -> Optional[Project]:
    db = get_database(strict=True)
    stmt = select(
        projects.c.slug, projects.c.name, projects.c.description, projects.c.created
    ).where(projects.c.slug == slug)

    result = await db.fetch_one(stmt)
    if result is None:
        return None

    return Project(
        slug=result.slug,
        name=result.name,
        description=result.description,
        created=result.created,
    )


async def list_projects() -> List[Project]:
    db = get_database(strict=True)
    stmt = select(
        projects.c.slug, projects.c.name, projects.c.description, projects.c.created
    )
    return [
        Project(
            slug=row.slug,
            name=row.name,
            description=row.description,
            created=row.created,
        )
        async for row in db.iterate(stmt)
    ]
