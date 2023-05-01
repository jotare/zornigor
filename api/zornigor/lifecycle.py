from zornigor.db.utility import create_database, get_database, set_database
from zornigor.settings import settings


async def initialize():
    # SQLite DB
    db = await create_database(settings.database_url)
    set_database(db)


async def finalize():
    db = get_database()
    if db is not None:
        await db.finalize()
