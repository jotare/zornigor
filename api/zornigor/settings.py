import os

from pydantic import BaseSettings

dir_path = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    database_url: str = "sqlite:///{}".format(
        os.path.abspath(os.path.join(dir_path, "..", "..", "db", "zornigor.db"))
    )


settings = Settings()
