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
    f"/{PROJECTS}/{{project_id}}",
    status_code=200,
    name="List projects",
    tags=["Projects"],
)
@version(1)
async def list_projects(request: Request) -> List[Project]:
    return [
        Project(
            id=1,
            name="Project 1",
            description="Description one",
        ),
        Project(
            id=2,
            name="Project 2",
            description="Description two",
        )
    ]
