import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.backend.core.utils import BASE_DIR


class Settings(BaseSettings):
    """A class for handling secrets fetched either from the .env file
    if it is present (local work) or from the environment (test / prod)."""

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=BASE_DIR.joinpath(".env"),
        env_file_encoding="utf8",
    )
    EXAMPLE_ENV_VARIABLE: str

    @classmethod
    def set_values(cls):
        return {
            key: os.getenv(key) or field.default or key
            for key, field in cls.model_fields.items()
        }


settings = Settings()
