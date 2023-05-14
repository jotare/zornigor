from datetime import datetime

import pytest

from zornigor.db.models import NewProject, Project, UpdateProject
from zornigor.db.projects import (
    create_project,
    get_project,
    list_projects,
    update_project,
)


def test_project_payloads():
    for field in NewProject.__fields__:
        assert field in Project.__fields__


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
async def test_create_project_default_dates(db):
    before = datetime.now()
    project = Project(
        slug="test-project",
        name="Test project",
        description="A test project for API tests",
    )
    await create_project(project)
    after = datetime.now()

    project = await get_project("test-project")
    assert project == project
    assert before < project.created and project.created < after
    assert before < project.modified and project.modified < after


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


@pytest.mark.asyncio
async def test_update_project(db, db_project: Project):
    updates = UpdateProject(name="Updated name", description="Updated description")
    await update_project(db_project.slug, updates)

    project = await get_project(db_project.slug)
    assert project.name == updates.name
    assert project.description == updates.description
