from typing import Optional

from databases import Database

_DATABASE: Optional[Database] = None


async def create_database(url: str) -> Database:
    db = Database(url)
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
