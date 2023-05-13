from sqlite3 import IntegrityError
from typing import List, Optional, Union

from sqlalchemy import and_, insert, select

from zornigor.db.errors import InvalidState
from zornigor.db.models import NewStory, Story
from zornigor.db.projects import get_project_last_story_id, update_project
from zornigor.db.tables import stories
from zornigor.db.utility import get_database


async def create_story(story: Union[Story, NewStory]):
    db = get_database(strict=True)  # type: ignore
    async with db.transaction():
        values = story.dict()

        if type(story) == NewStory:
            # use incremental story id by project
            last_story_id = await get_project_last_story_id(story.project)
            story_id = last_story_id + 1

            await update_project(story.project, last_story_id=story_id)
            values["id"] = story_id

        stmt = insert(stories).values(**values)
        try:
            result = await db.execute(stmt)
        except IntegrityError as exc:
            raise InvalidState(
                f"Invalid state '{story.state}' for story in project {story.project}"
            ) from exc

        return result


async def get_story(project: str, id: int) -> Optional[Story]:
    db = get_database(strict=True)  # type: ignore
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
    db = get_database(strict=True)  # type: ignore
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
