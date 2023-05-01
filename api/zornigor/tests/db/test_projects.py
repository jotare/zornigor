import pytest

from zornigor.db.models import Project
from zornigor.db.projects import list_projects, create_project, get_project


@pytest.mark.asyncio
async def test_create_project(db):
    project = Project(
        slug="test-project",
        description="Test project",
    )
    await create_project(project)

    project = await get_project("test-project")
    assert project == project


@pytest.mark.asyncio
async def test_list_projects(db):
    projects = [
        Project(slug="project-1"),
        Project(slug="project-2"),
        Project(slug="project-3"),
    ]
    for project in projects:
        await create_project(project)

    project_list = await list_projects()
    assert projects == project_list
