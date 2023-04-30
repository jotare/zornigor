import asyncio

from uvicorn.config import Config
from uvicorn.server import Server

from zornigor.app import app


def run():
    config = Config(app, port=8080, log_level="info")
    server = Server(config=config)

    asyncio.run(server.serve())


def run_dev():
    config = Config(app, port=8080, log_level="info", reload=True)
    server = Server(config=config)

    asyncio.run(server.serve())
