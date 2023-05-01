import os
from tempfile import mkdtemp

import pytest
from sqlalchemy import create_engine


from zornigor.db.tables import metadata
from zornigor.db.utility import create_database, set_database, forget_database


@pytest.fixture(scope="session")
def db_url() -> str:
    tmp = mkdtemp()
    return "sqlite:///{}".format(os.path.join(tmp, "test.db"))


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def db(db_url: str):
    engine = create_engine(db_url)
    metadata.create_all(engine)
    engine.dispose()

    db = await create_database(db_url)
    set_database(db)

    yield db

    forget_database()
    metadata.drop_all(engine)


@pytest.fixture(scope="function", autouse=True)
def test_settings(db_url: str):
    from zornigor.settings import settings

    settings.database_url = db_url


@pytest.fixture(scope="function", autouse=True)
def utilities():
    yield
    forget_database()
