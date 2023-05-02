from typing import List, Optional

from sqlalchemy import insert, select

from zornigor.db.models import Project
from zornigor.db.tables import projects
from zornigor.db.utility import get_database


async def create_project(project: Project):
    db = get_database(strict=True)
    stmt = insert(projects).values(
        slug=project.slug, name=project.name, description=project.description
    )
    await db.execute(stmt)


async def get_project(slug: str) -> Optional[Project]:
    db = get_database(strict=True)
    stmt = select(
        projects.c.slug, projects.c.name, projects.c.description, projects.c.created
    ).where(projects.c.slug == slug)
    result = await db.fetch_one(stmt)
    if result is None:
        return None
    (slug, name, description, created) = result
    return Project(slug=slug, name=name, description=description, created=created)


async def list_projects() -> List[Project]:
    db = get_database(strict=True)
    stmt = select(
        projects.c.slug, projects.c.name, projects.c.description, projects.c.created
    )
    results = await db.fetch_all(stmt)
    return [
        Project(slug=slug, name=name, description=description, created=created)
        for (slug, name, description, created) in results
    ]
