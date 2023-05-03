from typing import List

from fastapi_versioning import version
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from zornigor.api.models.story import CreateStory, Story
from zornigor.api.v1.router import PROJECT, STORIES, STORY, api
from zornigor.db import stories
from zornigor.db.models import Story as DbStory


@api.post(
    f"/{PROJECT}/{{project_id}}/{STORIES}",
    status_code=201,
    name="Create story",
    tags=["Stories"],
)
@version(1)
async def create_story(request: Request, project_id: str, item: CreateStory):
    s = DbStory(
        id=0,
        title=item.title,
        description=item.description,
        project=project_id,
        state=item.state,
    )
    await stories.create_story(s)
    return Response(status_code=201)


@api.get(
    f"/{PROJECT}/{{project_id}}/{STORIES}",
    status_code=200,
    name="List stories",
    tags=["Stories"],
)
@version(1)
async def list_stories(request: Request, project_id: str) -> List[Story]:
    return await stories.list_stories(project_id)


@api.get(
    f"/{PROJECT}/{{project_id}}/{STORY}/{{story_id}}",
    status_code=200,
    name="Get story",
    tags=["Stories"],
)
@version(1)
async def get_story(request: Request, project_id: str, story_id: str) -> Story:
    story = await stories.get_story(project_id, story_id)
    if story is None:
        return JSONResponse(
            status_code=404,
            content={
                "detail": f"Project '{project_id}' or story '{story_id}' not found"
            },
        )

    return Story(
        id=story.id,
        title=story.title,
        description=story.description,
        # creation=story.created,
        # modification=story.modified,
        project=story.project,
        state=story.state,
    )
