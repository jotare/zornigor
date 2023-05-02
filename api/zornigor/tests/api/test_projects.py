import pytest
from httpx import AsyncClient

from zornigor.api.models.project import CreateProject, Project
from zornigor.api.v1.router import PROJECT, PROJECTS


@pytest.mark.asyncio
async def test_create_project(api):
    payload = CreateProject(name="Zornigor Project", description="This is Zornigor")

    resp = await api.post(f"/{PROJECTS}", data=payload.json())
    assert resp.status_code == 201


@pytest.mark.asyncio
async def test_get_project(api, project):
    resp = await api.get(f"/{PROJECT}/{project.id}")
    assert resp.status_code == 200

    body = Project.parse_raw(resp.content)
    assert body.id == project.id
    assert body.name == project.name
    assert body.description == project.description


@pytest.mark.asyncio
async def test_get_nonexistent_project(api):
    resp = await api.get(f"/{PROJECT}/fake")
    assert resp.status_code == 404


# TODO: get 404, update, list
