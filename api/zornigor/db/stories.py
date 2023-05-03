from typing import List, Optional

from sqlalchemy import and_, insert, select

from zornigor.db.models import Story
from zornigor.db.tables import stories
from zornigor.db.utility import get_database


async def create_story(story: Story, force_id: bool = False):
    db = get_database(strict=True)
    values = story.dict()
    if not force_id:
        values.pop("id", None)
    stmt = insert(stories).values(**values)
    result = await db.execute(stmt)
    return result


async def get_story(project: str, id: int) -> Optional[Story]:
    db = get_database(strict=True)
    stmt = select(
        stories.c.id,
        stories.c.title,
        stories.c.description,
        stories.c.created,
        stories.c.modified,
        stories.c.project,
        stories.c.state,
    ).where(and_(stories.c.project == project, stories.c.id == id))

    result = await db.fetch_one(stmt)
    if result is None:
        return None

    return Story(
        id=result.id,
        title=result.title,
        description=result.description,
        created=result.created,
        modified=result.modified,
        project=result.project,
        state=result.state,
    )


async def list_stories(project: str) -> List[Story]:
    db = get_database(strict=True)
    stmt = select(
        stories.c.id,
        stories.c.title,
        stories.c.description,
        stories.c.created,
        stories.c.modified,
        stories.c.project,
        stories.c.state,
    ).where(stories.c.project == project)
    return [
        Story(
            id=row.id,
            title=row.title,
            description=row.description,
            created=row.created,
            modified=row.modified,
            project=row.project,
            state=row.state,
        )
        async for row in db.iterate(stmt)
    ]
