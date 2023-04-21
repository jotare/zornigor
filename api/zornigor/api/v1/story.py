from starlette.requests import Request
from fastapi_versioning import version

from zornigor.api.v1.router import api, STORIES, STORY


@api.get(
    f"/{STORIES}",
    status_code=200,
    name="List stories",
    tags=["Stories"],
)
@version(1)
async def list_stories(request: Request):
    return [
        {
            "id": 1,
            "name": "Story 1",
            "description": "Description",
        }
    ]
