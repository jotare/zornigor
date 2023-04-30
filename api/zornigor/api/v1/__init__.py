from fastapi_versioning import version

from . import project  # noqa
from . import state  # noqa
from . import story  # noqa
from .router import api


@api.get("/")
@version(1)
async def root():
    return {"message": "Welcome to Zornigor API v1"}
