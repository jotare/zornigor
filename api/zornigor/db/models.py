from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NewProject(BaseModel):
    slug: str
    name: str
    description: Optional[str]


class Project(BaseModel):
    slug: str
    name: str
    description: Optional[str]
    created: datetime
    last_story_id: int = Field(0, ge=0)


class State(BaseModel):
    slug: str
    name: str
    description: str = Field("")
    color: str
    project: str


class NewStory(BaseModel):
    title: str
    description: str
    created: datetime = Field(default_factory=datetime.now)
    modified: datetime = Field(default_factory=datetime.now)
    project: str
    state: str


class Story(BaseModel):
    id: int = Field(gt=0)
    title: str
    description: str
    created: datetime = Field(default_factory=datetime.now)
    modified: datetime = Field(default_factory=datetime.now)
    project: str
    state: str
