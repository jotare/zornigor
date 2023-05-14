from datetime import datetime
from typing import List, Optional, Union

from sqlalchemy import insert, select, update

from zornigor.db.errors import ProjectNotFound
from zornigor.db.models import NewProject, Project, UpdateProject
from zornigor.db.tables import projects
from zornigor.db.utility import get_database


async def create_project(project: Union[Project, NewProject]):
    db = get_database(strict=True)  # type: ignore
    stmt = insert(projects).values(**project.dict())
    await db.execute(stmt)


async def get_project(slug: str) -> Optional[Project]:
    db = get_database(strict=True)  # type: ignore
    stmt = select(
        projects.c.slug,
        projects.c.name,
        projects.c.description,
        projects.c.created,
        projects.c.modified,
        projects.c.last_story_id,
    ).where(projects.c.slug == slug)

    result = await db.fetch_one(stmt)
    if result is None:
        return None

    return Project(
        slug=result.slug,
        name=result.name,
        description=result.description,
        created=result.created,
        modified=result.modified,
        last_story_id=result.last_story_id,
    )


async def get_project_last_story_id(slug: str) -> int:
    db = get_database(strict=True)  # type: ignore
    stmt = select(projects.c.last_story_id).where(projects.c.slug == slug)
    project = await db.fetch_one(stmt)
    if project is None:
        raise ProjectNotFound(f"Project {slug} not found")
    return project.last_story_id


async def list_projects() -> List[Project]:
    db = get_database(strict=True)  # type: ignore
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


async def update_project_last_story_id(slug: str, last_story_id: int):
    db = get_database(strict=True)  # type: ignore
    stmt = (
        update(projects)
        .where(projects.c.slug == slug)
        .values(last_story_id=last_story_id)
    )
    await db.execute(stmt)


async def update_project(slug: str, project: UpdateProject):
    db = get_database(strict=True)  # type: ignore
    values = project.dict()
    values["modified"] = datetime.now()
    stmt = update(projects).where(projects.c.slug == slug).values(**values)
    await db.execute(stmt)
