import pytest
from httpx import AsyncClient

from zornigor.api.models.project import CreateProject, Project
from zornigor.api.v1.router import PROJECT, PROJECTS


@pytest.mark.asyncio
async def test_create_project(api: AsyncClient):
    payload = CreateProject(name="Zornigor Project", description="This is Zornigor")

    resp = await api.post(f"/{PROJECTS}", data=payload.json())
    assert resp.status_code == 201


@pytest.mark.asyncio
async def test_get_project(api: AsyncClient, api_project: Project):
    resp = await api.get(f"/{PROJECT}/{api_project.id}")
    assert resp.status_code == 200

    body = Project.parse_raw(resp.content)
    assert body.id == api_project.id
    assert body.name == api_project.name
    assert body.description == api_project.description


@pytest.mark.asyncio
async def test_get_nonexistent_project(api: AsyncClient):
    resp = await api.get(f"/{PROJECT}/fake")
    assert resp.status_code == 404


# TODO: update, list
