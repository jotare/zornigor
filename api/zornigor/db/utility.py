import sqlite3
from typing import Optional

from databases import Database

_DATABASE: Optional[Database] = None


class _Connection(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.execute("PRAGMA foreign_keys = ON")


async def create_database(url: str) -> Database:
    # HACK: `factory` is passed as kwarg. It'll be propagated to aiosqlite
    # backend and it'll be used as sqlite3.Connection object creation. We
    # override this to be able to set `PRAGMA foreign_keys=ON` for every
    # connection to the database.
    db = Database(url, factory=_Connection)
    await db.connect()
    return db


def get_database(*, strict: bool = False) -> Optional[Database]:
    global _DATABASE

    if strict and _DATABASE is None:
        raise ValueError("Database not configured")

    return _DATABASE


def set_database(db: Database, *, force: bool = False):
    global _DATABASE
    if _DATABASE is not None and not force:
        raise ValueError("Database already set")
    _DATABASE = db


def forget_database():
    global _DATABASE
    _DATABASE = None
