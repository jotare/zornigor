from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Project(BaseModel):
    slug: str
    name: str
    description: Optional[str]
    created: datetime = Field(default_factory=datetime.now)


class State(BaseModel):
    slug: str
    name: str
    description: str = Field("")
    color: str
    project: str


class Story(BaseModel):
    id: int
    title: str
    description: str
    created: datetime = Field(default_factory=datetime.now)
    modified: datetime = Field(default_factory=datetime.now)
    project: str
    state: str
