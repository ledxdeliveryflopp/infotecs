from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class UrlSettings(BaseSettings):
    """Настройки url api"""
    api_url: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Settings(BaseSettings):
    url_settings: UrlSettings


@lru_cache()
def init_settings():
    """Инициализация настроек"""
    all_settings = Settings(url_settings=UrlSettings())
    return all_settings


settings = init_settings()
