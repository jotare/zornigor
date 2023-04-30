from typing import List

from fastapi_versioning import version
from starlette.requests import Request

from zornigor.api.models.state import State
from zornigor.api.v1.router import PROJECTS, STATES, api


@api.get(
    f"/{PROJECTS}/{{project_id}}/{STATES}",
    status_code=200,
    name="List states",
    tags=["States"],
)
@version(1)
async def list_states(request: Request, project_id: str) -> List[State]:
    # TODO implement non hardcoded states
    return [
        State(
            id="ideas",
            name="Ideas",
            description="Ideas to work on some day",
        ),
        State(
            id="backlog",
            name="Backlog",
            description="Backlog of stories to work on in a not far future",
        ),
        State(
            id="todo",
            name="ToDo",
            description="Things to do soon",
        ),
        State(
            id="dev",
            name="In development",
            description="Stories in progress",
        ),
        State(
            id="blocked",
            name="Blocked",
            description="Blocked by someone or something",
        ),
        State(
            id="done",
            name="Done",
            description="Completed stories",
        ),
    ]
