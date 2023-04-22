from fastapi_versioning import version

from . import story
from .router import api


@api.get("/")
@version(1)
async def root():
    return {
        "message": "Welcome to Zornigor API v1"
    }
