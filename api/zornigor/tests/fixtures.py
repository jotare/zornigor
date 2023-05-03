import os
from tempfile import mkdtemp

import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine

from zornigor.api.models.project import CreateProject, Project
from zornigor.api.models.story import CreateStory, Story
from zornigor.api.v1.router import PROJECT, PROJECTS, STORIES, STORY
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


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def project(api):
    payload = CreateProject(
        id="zornigor",
        name="Zornigor Project",
        description="This is Zornigor",
    )

    resp = await api.post(f"/{PROJECTS}", data=payload.json())
    assert resp.status_code == 201

    resp = await api.get(f"/{PROJECT}/zornigor")
    assert resp.status_code == 200

    yield Project.parse_raw(resp.content)


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def story(api: AsyncClient, project: Project):
    payload = CreateStory(
        title="Story one", description="Story one description", state="todo"
    )
    resp = await api.post(f"/{PROJECT}/{project.id}/{STORIES}", data=payload.json())
    assert resp.status_code == 201

    resp = await api.get(f"/{PROJECT}/{project.id}/{STORY}/1")
    assert resp.status_code == 200

    yield Story.parse_raw(resp.content)
