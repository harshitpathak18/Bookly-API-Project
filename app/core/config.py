from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",             # Tell Pydantic to load from .env
        extra="ignore"               # Ignore unknown env vars (optional)
    )

# Single instance of settings to be reused everywhere
settings = Settings()
