from typing import List
from uuid import uuid4

from zornigor.db.models import NewProject
from zornigor.db.projects import create_project


def generate_project() -> NewProject:
    id = str(uuid4())
    project = NewProject(
        slug=id,
        name=f"generated-project:{id}",
        description=f"Generated project {id}",
    )
    return project


async def create_projects(n: int) -> List[NewProject]:
    projects = []
    for _ in range(n):
        payload = generate_project()
        await create_project(payload)
        projects.append(payload)
    return projects
