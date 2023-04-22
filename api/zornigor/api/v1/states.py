from starlette.requests import Request
from fastapi_versioning import version

from zornigor.api.v1.router import api, STATES, STATE
from zornigor.api.models.state import State


@api.get(
    f"/{STATES}",
    status_code=200,
    name="List states",
    tags=["States"],
)
@version(1)
async def list_states(request: Request) -> List[State]:
    # TODO implement non hardcoded states
    return [
        State(
            name="Ideas",
            description="Ideas to work on some day",
        ),
        State(
            name="Backlog",
            description="Backlog of stories to work on in a not far future",
        ),
        State(
            name="ToDo",
            description="Things to do soon",
        ),
        State(
            name="In development",
            description="Stories in progress",
        ),
        State(
            name="Blocked",
            description="Blocked by someone or something",
        ),
        State(
            name="Done",
            description="Completed stories",
        ),
    ]
