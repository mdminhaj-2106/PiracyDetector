from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent



class Settings(BaseSettings):
    PROJECT_NAME: str = "Piracy Detector"
    DEBUG: bool = True
    DATABASE_URL: str = ""
    CLIENT_SECRETS_PATH: str = ""
    model_config = SettingsConfigDict(env_file = BASE_DIR / ".env")


settings = Settings()