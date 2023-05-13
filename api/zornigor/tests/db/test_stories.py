from typing import List

import pytest

from zornigor.db.errors import InvalidState, ProjectNotFound
from zornigor.db.models import NewStory, Project, State, Story
from zornigor.db.states import create_state
from zornigor.db.stories import create_story, get_story
from zornigor.tests.db import utils


@pytest.fixture(scope="function")
def project(db_project: Project) -> str:
    return db_project.slug


@pytest.mark.asyncio
async def test_create_story(db, project: str, db_states: List[str]):
    story = NewStory(
        title="Story",
        description="Description",
        project="zornigor",
        state=db_states[0],
    )
    await create_story(story)


@pytest.mark.asyncio
async def test_create_story_with_invalid_project(db):
    story = NewStory(
        title="Story", description="Description", project="INVALID", state="INVALID"
    )
    with pytest.raises(ProjectNotFound):
        await create_story(story)


@pytest.mark.asyncio
async def test_create_story_with_invalid_state(db, project: str):
    story = NewStory(
        title="Story", description="Description", project=project, state="INVALID"
    )
    with pytest.raises(InvalidState):
        await create_story(story)


@pytest.mark.asyncio
async def test_story_ids_independent_per_project(db):
    project_1, project_2 = await utils.create_projects(2)

    state = State(slug="todo", name="ToDo", project="---")
    story = Story(
        id=1, title="story", description="A story", project="---", state=state.slug
    )

    state.project = story.project = project_1.slug
    await create_state(state)
    await create_story(story)

    state.project = story.project = project_2.slug
    await create_state(state)
    await create_story(story)

    story_one = await get_story(project_1.slug, 1)
    story_two = await get_story(project_2.slug, 1)

    assert story_one is not None
    assert story_two is not None
