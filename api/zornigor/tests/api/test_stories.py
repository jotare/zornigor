from typing import List

import pytest
from httpx import AsyncClient

from zornigor.api.models.project import Project
from zornigor.api.models.story import CreateStory, Story
from zornigor.api.v1.router import PROJECT, STORIES, STORY


@pytest.mark.asyncio
async def test_create_story(
    api: AsyncClient, api_project: Project, api_states: List[str]
):
    payload = CreateStory(
        title="Story title", description="Story description", state=api_states[0]
    )
    resp = await api.post(f"/{PROJECT}/{api_project.id}/{STORIES}", data=payload.json())
    assert resp.status_code == 201


@pytest.mark.asyncio
async def test_create_story_with_invalid_state(api: AsyncClient, api_project: Project):
    payload = CreateStory(
        title="Story title", description="Story description", state="INVALID"
    )
    resp = await api.post(f"/{PROJECT}/{api_project.id}/{STORIES}", data=payload.json())
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_get_story(api: AsyncClient, api_project: Project, api_story: Story):
    resp = await api.get(f"/{PROJECT}/{api_project.id}/{STORY}/{api_story.id}")
    assert resp.status_code == 200

    body = Story.parse_raw(resp.content)
    assert body.id == api_story.id
    assert body.title == api_story.title
    assert body.description == api_story.description
    assert body.project == api_project.id


@pytest.mark.asyncio
async def test_get_nonexistent_project_story(api: AsyncClient):
    resp = await api.get(f"/{PROJECT}/fake")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_nonexistent_story(api: AsyncClient, api_project: Project):
    resp = await api.get(f"/{PROJECT}/{api_project.id}/{STORY}/123")
    assert resp.status_code == 404


# TODO: update, list, delete
