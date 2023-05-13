from typing import List, Optional

from pydantic import BaseModel, Field

from zornigor.api.models.common import Slug
from zornigor.api.models.state import State


class CreateProject(BaseModel):
    id: Optional[Slug] = None
    name: str = Field(min_length=1)
    description: str
    states: List[State] = []


class Project(BaseModel):
    id: Slug
    name: str
    description: str
