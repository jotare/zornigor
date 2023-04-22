from pydantic import BaseModel


class CreateProject(BaseModel):
    name: str
    description: str


class Project(BaseModel):
    id: str
    slug: str
    name: str
    description: str
