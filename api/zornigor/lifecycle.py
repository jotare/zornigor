from zornigor.db.utility import create_database, forget_database, set_database
from zornigor.settings import settings


async def initialize():
    # SQLite DB
    db = await create_database(settings.database_url)
    set_database(db)


async def finalize():
    forget_database()
