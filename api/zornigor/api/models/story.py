from pydantic import BaseModel


class CreateStory(BaseModel):
    title: str
    description: str


class Story(BaseModel):
    id: int

    title: str
    description: str

    state: str

    # creation: datetime
    # modification: datetime
