from typing import List
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).resolve().parent.parent.parent



class Settings(BaseSettings):
    PROJECT_NAME: str = "Piracy Detector"
    DEBUG: bool = True
    DATABASE_URL: str = ""
    CLIENT_SECRETS_PATH: str = ""
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GOOGLE_ACCESS_TOKEN: str = ""
    GOOGLE_REFRESH_TOKEN: str = ""
    SCOPES: List[str] = [
        "https://www.googleapis.com/auth/youtube.readonly"
    ]
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore"
    )


settings = Settings()