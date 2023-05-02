from typing import List

from fastapi_versioning import version
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from zornigor.api.models.project import CreateProject, Project
from zornigor.api.v1.router import PROJECT, PROJECTS, api
from zornigor.db import projects
from zornigor.db.models import Project as DbProject
from zornigor.utils import slugify


@api.post(
    f"/{PROJECTS}",
    status_code=201,
    name="Create project",
    tags=["Projects"],
)
@version(1)
async def create_project(request: Request, item: CreateProject):
    p = DbProject(
        slug=slugify(item.id) if item.id else slugify(item.name),
        name=item.name,
        description=item.description,
    )
    await projects.create_project(p)
    return Response(status_code=201)


@api.get(
    f"/{PROJECTS}",
    status_code=200,
    name="List projects",
    tags=["Projects"],
)
@version(1)
async def list_projects(request: Request) -> List[Project]:
    return [
        Project(id=p.slug, name=p.name, description=p.description)
        for p in await projects.list_projects()
    ]


@api.get(
    f"/{PROJECT}/{{project_id}}",
    status_code=200,
    name="Get project",
    tags=["Projects"],
)
@version(1)
async def get_project(request: Request, project_id: str) -> Project:
    project = await projects.get_project(slug=project_id)
    if project is None:
        return JSONResponse(
            status_code=404, content={"detail": f"Project '{project_id}' not found"}
        )

    return Project(
        id=project.slug,
        name=project.name,
        description=project.description,
    )
