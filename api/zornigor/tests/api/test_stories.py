import pytest
from httpx import AsyncClient

from zornigor.api.models.project import CreateProject, Project
from zornigor.api.models.story import CreateStory, Story
from zornigor.api.v1.router import PROJECT, PROJECTS, STORIES, STORY


@pytest.mark.asyncio
async def test_create_story(api: AsyncClient, project: Project):
    payload = CreateStory(
        title="Story title", description="Story description", state="todo"
    )
    resp = await api.post(f"/{PROJECT}/{project.id}/{STORIES}", data=payload.json())
    assert resp.status_code == 201


@pytest.mark.asyncio
async def test_get_project(api: AsyncClient, project: Project, story: Story):
    resp = await api.get(f"/{PROJECT}/{project.id}/{STORY}/{story.id}")
    assert resp.status_code == 200

    body = Story.parse_raw(resp.content)
    assert body.id == story.id
    assert body.title == story.title
    assert body.description == story.description
    assert body.project == project.id


@pytest.mark.asyncio
async def test_get_nonexistent_project_story(api: AsyncClient):
    resp = await api.get(f"/{PROJECT}/fake")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_nonexistent_story(api: AsyncClient, project: Project):
    resp = await api.get(f"/{PROJECT}/{project.id}/{STORY}/123")
    assert resp.status_code == 404


# TODO: update, list
