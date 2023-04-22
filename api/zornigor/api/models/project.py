from pydantic import BaseModel


class CreateProject(BaseModel):
    name: str
    description: str


class Project(BaseModel):
    slug: str
    name: str
    description: str
