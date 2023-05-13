import sqlite3

import pytest
from pydantic import ValidationError

from zornigor.db.models import Project, State
from zornigor.db.states import create_state
from zornigor.tests.db import utils


@pytest.fixture(scope="function")
def project(db_project: Project) -> str:
    return db_project.slug


@pytest.mark.asyncio
async def test_create_state(db, project: str):
    state = State(
        slug="todo",
        name="To Do",
        description="Things to do",
        project=project,
        color="FF00FF",
    )
    await create_state(state)


@pytest.mark.asyncio
async def test_create_state_twice(db, project: str):
    state = State(
        slug="todo",
        name="To Do",
        description="Things to do",
        project=project,
        color="FF00FF",
    )
    await create_state(state)

    with pytest.raises(sqlite3.IntegrityError):
        await create_state(state)


@pytest.mark.asyncio
async def test_create_state_in_nonexistent_project(db):
    state = State(
        slug="todo",
        name="To Do",
        description="Things to do",
        project="INVALID-PROJECT",
        color="FF00FF",
    )
    with pytest.raises(sqlite3.IntegrityError):
        await create_state(state)


@pytest.mark.asyncio
async def test_create_same_state_in_different_projects(db):
    state = State(
        slug="todo",
        name="To Do",
        description="Things to do",
        project="---",
        color="FF00FF",
    )
    project_1, project_2 = await utils.create_projects(2)

    state.project = project_1.slug
    await create_state(state)

    state.project = project_2.slug
    await create_state(state)


@pytest.mark.asyncio
async def test_create_state_with_invalid_color(db, project: str):
    with pytest.raises(ValidationError):
        State(
            slug="todo",
            name="To Do",
            description="Things to do",
            project=project,
            color="COLOR_SHOULD_BE_IN_HEX_NOTATION",
        )
