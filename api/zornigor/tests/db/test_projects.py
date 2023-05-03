import pytest

from zornigor.db.models import Project
from zornigor.db.projects import create_project, get_project, list_projects


@pytest.mark.asyncio
async def test_create_project(db):
    project = Project(
        slug="test-project",
        name="Test project",
        description="A test project for API tests",
    )
    await create_project(project)

    project = await get_project("test-project")
    assert project == project


@pytest.mark.asyncio
async def test_list_projects(db):
    projects = [
        Project(slug="project-1", name="Project 1"),
        Project(slug="project-2", name="Project 2"),
        Project(slug="project-3", name="Project 3"),
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
