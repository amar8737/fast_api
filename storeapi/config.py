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
