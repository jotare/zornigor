from typing import Optional

from pydantic import BaseModel, Field

from zornigor.api.models.common import Slug


class CreateProject(BaseModel):
    id: Optional[Slug] = None
    name: str = Field(min_length=1)
    description: str


class Project(BaseModel):
    id: Slug
    name: str
    description: str
