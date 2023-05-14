from datetime import datetime

from pydantic import BaseModel


class CreateStory(BaseModel):
    title: str
    description: str
    state: str


class UpdateStory(BaseModel):
    title: str
    description: str
    state: str


class Story(BaseModel):
    id: int

    title: str
    description: str

    # creation: datetime
    # modification: datetime

    project: str
    state: str
