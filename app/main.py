"""Application entry point — creates and configures the FastAPI app."""

from fastapi import FastAPI
from app.api import router
from app.utils import APP_NAME, APP_VERSION

app = FastAPI(title=APP_NAME, version=APP_VERSION)
app.include_router(router)
