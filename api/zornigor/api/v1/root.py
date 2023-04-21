from fastapi_versioning import version

from zornigor.api.v1.router import api


@api.get("/")
@version(1)
async def root():
    return {
        "message": "Welcome to Zornigor API v1"
    }
