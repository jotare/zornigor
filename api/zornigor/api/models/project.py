from pydantic import BaseModel

from zornigor.api.models.common import Slug


class CreateProject(BaseModel):
    name: str
    description: str


class Project(BaseModel):
    id: Slug
    name: str
    description: str
