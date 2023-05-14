from typing import List

import pytest

from zornigor.db.errors import InvalidState, ProjectNotFound
from zornigor.db.models import NewStory, Project, State, Story, UpdateStory
from zornigor.db.states import create_state
from zornigor.db.stories import create_story, get_story, update_story, delete_story
from zornigor.tests.db import utils


@pytest.fixture(scope="function")
def project(db_project: Project) -> str:
    return db_project.slug


@pytest.mark.asyncio
async def test_create_story(db, project: str, db_states: List[str]):
    story = NewStory(
        title="Story",
        description="Description",
        project=project,
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
async def test_create_story_ids_independent_per_project(db):
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


@pytest.mark.asyncio
async def test_get_story(db, db_story: Story):
    story = await get_story(db_story.project, db_story.id)
    assert story is not None


@pytest.mark.asyncio
async def test_get_nonexistent_story(db, db_project: Project):
    story = await get_story(db_project.slug, "INVALID")
    assert story is None


@pytest.mark.asyncio
async def test_update_story(
    db, db_project: Project, db_story: Story, db_states: List[str]
):
    updates = UpdateStory(
        title="Updated title",
        description="Updated description",
        state=db_states[1],
    )
    await update_story(db_project.slug, updates)

    story = await get_story(db_project.slug, db_story.id)
    assert story.title == updates.title
    assert story.description == updates.description
    assert story.state == updates.state


@pytest.mark.asyncio
async def test_delete_story(db, db_story: Story):
    await delete_story(db_story.project, db_story.id)

    story = await get_story(db_story.project, db_story.id)
    assert story is None
