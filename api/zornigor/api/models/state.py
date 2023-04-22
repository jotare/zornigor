from typing import Optional

from pydantic import BaseModel



class State(BaseModel):
    name: str
    description: Optional[str]
