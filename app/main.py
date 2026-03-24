from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

origins = [
    "http://localhost:5173",
]