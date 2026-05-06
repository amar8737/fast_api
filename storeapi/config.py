from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV_STATE: str = "dev"
    model_config = SettingsConfigDict(env_file=".env")


class GlobalSettings(Settings):
    database_url: str
    DB_FORCE_ROLLBACK: bool = False


class DevSettings(GlobalSettings):
    model_config = SettingsConfigDict(env_file=".env.dev")


class ProdSettings(GlobalSettings):
    model_config = SettingsConfigDict(env_file=".env.prod")


class TestSettings(GlobalSettings):
    model_config = SettingsConfigDict(env_file=".env.test")


@lru_cache
def get_settings() -> GlobalSettings:
    env_state = Settings().ENV_STATE

    settings_map = {
        "dev": DevSettings,
        "prod": ProdSettings,
        "test": TestSettings,
    }

    return settings_map.get(env_state, DevSettings)()


settings = get_settings()
