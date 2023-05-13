import os
from datetime import datetime
from tempfile import mkdtemp
from typing import List

import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine

from zornigor.api import models as api_models
from zornigor.api.v1.router import PROJECT, PROJECTS, STORIES, STORY
from zornigor.db import models as db_models
from zornigor.db.projects import create_project
from zornigor.db.states import create_state
from zornigor.db.tables import metadata
from zornigor.db.utility import create_database, forget_database, set_database


@pytest.fixture(scope="session")
def db_url() -> str:
    tmp = mkdtemp()
    return "sqlite:///{}".format(os.path.join(tmp, "test.db"))


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def db(db_url: str):
    engine = create_engine(db_url)
    metadata.create_all(engine)
    engine.dispose()

    db = await create_database(db_url)
    set_database(db)

    yield db

    forget_database()
    metadata.drop_all(engine)


@pytest.fixture(scope="function", autouse=True)
def test_settings(db_url: str):
    from zornigor.settings import settings

    settings.database_url = db_url


@pytest.fixture(scope="function", autouse=True)
def utilities():
    yield
    forget_database()


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def api(db):
    from zornigor.app import app

    # await app.router.startup()

    base_url = "http://test/api/v1"
    client = AsyncClient(app=app, base_url=base_url)

    yield client

    # await app.router.shutdown()


@pytest.fixture
@pytest.mark.asyncio
async def db_project(db) -> db_models.Project:
    project = db_models.Project(
        slug="zornigor",
        name="Zornigor Project",
        description="This is Zornigor",
        created=datetime.now(),
    )
    await create_project(project)
    yield project


@pytest.fixture
@pytest.mark.asyncio
async def api_project(api) -> api_models.Project:
    payload = api_models.CreateProject(
        id="zornigor",
        name="Zornigor Project",
        description="This is Zornigor",
    )

    resp = await api.post(f"/{PROJECTS}", data=payload.json())
    assert resp.status_code == 201

    resp = await api.get(f"/{PROJECT}/zornigor")
    assert resp.status_code == 200

    yield api_models.Project.parse_raw(resp.content)


async def _states(project: str):
    states = [
        db_models.State(
            slug="todo",
            name="ToDo",
            description="Things to do soon",
            project=project,
        ),
        db_models.State(
            slug="wip",
            name="Work in progress",
            description="Stories in progress",
            project=project,
        ),
        db_models.State(
            slug="done",
            name="Done",
            description="Completed stories",
            project=project,
        ),
    ]

    for state in states:
        await create_state(state)

    return [state.slug for state in states]


@pytest.fixture
@pytest.mark.asyncio
async def db_states(db, db_project: db_models.Project):
    yield await _states(db_project.slug)


@pytest.fixture
@pytest.mark.asyncio
async def api_states(db, api_project: api_models.Project):
    yield await _states(api_project.id)


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def api_story(
    api: AsyncClient, api_project: api_models.Project, api_states: List[str]
):
    payload = api_models.CreateStory(
        title="Story one", description="Story one description", state=api_states[0]
    )
    resp = await api.post(f"/{PROJECT}/{api_project.id}/{STORIES}", data=payload.json())
    assert resp.status_code == 201

    resp = await api.get(f"/{PROJECT}/{api_project.id}/{STORY}/1")
    assert resp.status_code == 200

    yield api_models.Story.parse_raw(resp.content)
