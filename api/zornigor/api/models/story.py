from pydantic import BaseModel


class CreateStory(BaseModel):
    title: str
    description: str


class Story(BaseModel):
    # Content
    title: str
    description: str

    # Metadata
    creation: datetime
    modification: datetime
