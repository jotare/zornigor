from datetime import datetime

import pytest

from zornigor.db.models import NewProject, Project
from zornigor.db.projects import create_project, get_project, list_projects


def test_project_payloads():
    for field in NewProject.__fields__:
        assert field in Project.__fields__


@pytest.mark.asyncio
async def test_create_project(db):
    project = Project(
        slug="test-project",
        name="Test project",
        description="A test project for API tests",
        created=datetime.now(),
    )
    await create_project(project)

    project = await get_project("test-project")
    assert project == project


@pytest.mark.asyncio
async def test_list_projects(db):
    projects = [
        NewProject(slug="project-1", name="Project 1"),
        NewProject(slug="project-2", name="Project 2"),
        NewProject(slug="project-3", name="Project 3"),
    ]
    for project in projects:
        await create_project(project)

    project_list = await list_projects()
    assert len(project_list) == len(projects)
    for i in range(len(projects)):
        payload = projects[i]
        fetched = project_list[i]

        assert payload.slug == fetched.slug
        assert payload.name == fetched.name
        assert fetched.description is None
