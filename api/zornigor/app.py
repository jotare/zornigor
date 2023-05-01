from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from zornigor.api.v1.router import api as api_v1
from zornigor.lifecycle import finalize, initialize

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8081"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

settings = dict(
    middleware=middleware,
    on_startup=[initialize],
    on_shutdown=[finalize],
)

base_app = FastAPI(title="Zornigor API", **settings)


@base_app.get("/")
async def root():
    return {"message": "Welcome to Zornigor API v1"}


base_app.include_router(api_v1)

app = VersionedFastAPI(
    base_app,
    version_format="{major}",
    prefix_format="/api/v{major}",
    default_version=(1, 0),
    enable_latest=True,
    **settings,
)
