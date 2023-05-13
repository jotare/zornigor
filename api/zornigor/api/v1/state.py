from typing import List

from fastapi_versioning import version
from starlette.requests import Request

from zornigor.api.models.common import Slug
from zornigor.api.models.state import State
from zornigor.api.v1.router import PROJECT, STATES, api
from zornigor.db import states


@api.get(
    f"/{PROJECT}/{{project_id}}/{STATES}",
    status_code=200,
    name="List states",
    tags=["States"],
)
@version(1)
async def list_states(request: Request, project_id: str) -> List[State]:
    db_states = await states.list_states(project_id)
    return [
        State(
            id=Slug(db_state.slug),
            name=db_state.name,
            description=db_state.description,
        )
        for db_state in db_states
    ]
