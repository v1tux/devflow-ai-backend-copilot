from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "DevFlow AI"
    APP_ENV: str = "development"
    SECRET_KEY: str = "change-this-secret"
    DATABASE_URL: str = "sqlite:///./devflow.db"
    OPENAI_API_KEY: str | None = None
    CORS_ORIGINS: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

    @property
    def cors_list(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
