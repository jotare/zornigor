from typing import Optional

from pydantic import BaseModel

from zornigor.api.models.common import Slug


class State(BaseModel):
    id: Slug
    name: str
    description: Optional[str]
