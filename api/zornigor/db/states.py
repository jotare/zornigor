from typing import List, Optional

from sqlalchemy import and_, insert, select

from zornigor.db.models import State
from zornigor.db.tables import states
from zornigor.db.utility import get_database


async def create_state(state: State):
    db = get_database(strict=True)  # type: ignore
    values = state.dict()
    values["color"] = state.color.as_hex()
    stmt = insert(states).values(**values)
    await db.execute(stmt)


async def get_state(project: str, slug: str) -> Optional[State]:
    db = get_database(strict=True)  # type: ignore
    stmt = select(
        states.c.slug,
        states.c.name,
        states.c.description,
        states.c.color,
        states.c.project,
    ).where(and_(states.c.project == project, states.c.slug == slug))

    result = await db.fetch_one(stmt)
    if result is None:
        return None

    return State(
        slug=result.slug,
        name=result.name,
        description=result.description,
        color=result.color,
        project=result.project,
    )


async def list_states(project: str) -> List[State]:
    db = get_database(strict=True)  # type: ignore
    stmt = select(
        states.c.slug,
        states.c.name,
        states.c.description,
        states.c.color,
        states.c.project,
    ).where(states.c.project == project)
    return [
        State(
            slug=row.slug,
            name=row.name,
            description=row.description,
            color=row.color,
            project=row.project,
        )
        async for row in db.iterate(stmt)
    ]
