# -*- coding: utf-8 -*-

import os
from pathlib import Path
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POOL_SIZE: int = Field(10)
    SQLALCHEMY_URL_ASYNC: str = Field()
    SQLALCHEMY_URL_SYNC: str = Field()
    SENTRY_DSN: str = Field("")

    class Config:
        env_file = os.path.join(Path(__file__).parent.parent.parent, ".env")
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    return Settings()
