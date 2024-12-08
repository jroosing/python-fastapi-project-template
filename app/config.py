import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

DOTENV = os.path.join(os.path.dirname(__file__), ".env")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="utf-8")

    postgres_port: int = Field(alias="POSTGRES_PORT")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD")
    postgres_user: str = Field(alias="POSTGRES_USER")
    postgres_db: str = Field(alias="POSTGRES_DB")
    postgres_host: str = Field(alias="POSTGRES_HOST")

settings = Settings()
