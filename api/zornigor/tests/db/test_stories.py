from typing import List

import pytest

from zornigor.db.models import NewProject, NewStory, Project, State, Story
from zornigor.db.projects import create_project
from zornigor.db.stories import create_story, get_story, list_stories


@pytest.fixture
@pytest.mark.asyncio
async def project(db):
    project = NewProject(
        slug="test-project",
        name="Test project",
        description="A test project for API tests",
    )
    await create_project(project)
    yield "test-project"


@pytest.fixture
@pytest.mark.asyncio
async def states(db):
    yield ["todo", "wip", "done"]


@pytest.mark.asyncio
async def test_create_story(db, project: str, states: List[str]):
    story = NewStory(
        title="Story",
        description="Description",
        project=project,
        state=states[0],
    )
    await create_story(story)


@pytest.mark.asyncio
async def test_story_ids_independent_per_project(db, states):
    projects = [
        NewProject(
            slug="one",
            name="Project one",
        ),
        NewProject(
            slug="two",
            name="Project one",
        ),
    ]
    for project in projects:
        await create_project(project)

    story = Story(
        id=1,
        title="Story",
        description="Description",
        project="---",
        state=states[0],
    )

    story.project = "one"
    await create_story(story)
    story.project = "two"
    await create_story(story)

    story_one = get_story("one", 1)
    story_two = get_story("one", 1)
