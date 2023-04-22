from typing import Union

from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount

from zornigor.api.v1.router import api as api_v1


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:8081"
        ],
        allow_methods=["*"],
        allow_headers=["*"],

    )
]

settings = dict(
    middleware=middleware,
)

base_app = FastAPI(title="Zornigor API", **settings)

@base_app.get("/")
async def root():
    return {
        "message": "Welcome to Zornigor API v1"
    }

base_app.include_router(api_v1)

def extend_openapi(app: Union[FastAPI, Mount]):  # pragma: no cover
    for route in app.routes:
        # mypy complains about BaseRoute not having endpoint and
        # description attributes, but routes passed here always have
        if hasattr(route.endpoint, "__required_scopes__"):  # type: ignore
            scopes = route.endpoint.__required_scopes__  # type: ignore


extend_openapi(base_app)

app = VersionedFastAPI(
    base_app,
    version_format="{major}",
    prefix_format="/api/v{major}",
    default_version=(1, 0),
    enable_latest=True,
    **settings,
)
