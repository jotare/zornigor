from starlette.requests import Request
from fastapi_versioning import version

from zornigor.api.v1.router import api, PROJECTS, PROJECT
from zornigor.api.models.project import Project


@api.post(
    f"/{PROJECTS}",
    status_code=201,
    name="Create project",
    tags=["Projects"],
)
@version(1)
async def create_project(request: Request) -> Project:
    raise NotImplementedError()


@api.get(
    f"/{PROJECTS}",
    status_code=200,
    name="List projects",
    tags=["Projects"],
)
@version(1)
async def list_projects(request: Request) -> List[Project]:
    return [
        Project(
            slug="project-1",
            name="Project 1",
            description="Description one",
        ),
        Project(
            slug="project-2",
            name="Project 2",
            description="Description two",
        )
    ]


@api.get(
    f"/{PROJECTS}/{{project_slug}}",
    status_code=200,
    name="Get project",
    tags=["Projects"],
)
@version(1)
async def get_project(request: Request, project_slug: str) -> Project:
    return Project(
        slug=project_slug,
        name=f"Project: {project_slug}",
        description="Description for {project_slug}",
    )
