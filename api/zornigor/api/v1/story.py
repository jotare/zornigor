from typing import List

from starlette.requests import Request
from fastapi_versioning import version

from zornigor.api.v1.router import api, PROJECTS, STORIES, STORY
from zornigor.api.models.story import Story


@api.post(
    f"/{PROJECTS}/{{project_id}}/{STORIES}",
    status_code=201,
    name="Create story",
    tags=["Stories"],
)
@version(1)
async def create_story(request: Request) -> Story:
    raise NotImplementedError()


@api.get(
    f"/{PROJECTS}/{{project_id}}/{STORIES}",
    status_code=200,
    name="List stories",
    tags=["Stories"],
)
@version(1)
async def list_stories(request: Request) -> List[Story]:
    return [
        Story(
            id=1,
            title="Story 1",
            description="Description one",
            state="todo"
        ),
        Story(
            id=2,
            title="Story 2",
            description="Description two",
            state="dev"
        ),
        Story(
            id=3,
            title="Story 3",
            description="Description three",
            state="blocked",
        ),
        Story(
            id=4,
            title="Story 4",
            description="Description four",
            state="done",
        ),
        Story(
            id=5,
            title="Story 5",
            description="Description five",
            state="done",
        ),
    ]
