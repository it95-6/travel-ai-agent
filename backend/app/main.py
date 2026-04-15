from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(api_router)
