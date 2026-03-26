"""API router: health and version endpoints."""

from fastapi import APIRouter
from app.utils import build_status_payload, build_version_payload

router = APIRouter()


@router.get("/health")
def health() -> dict:
    """Return service health status."""
    return build_status_payload("ok")


@router.get("/version")
def version() -> dict:
    """Return application name and version."""
    return build_version_payload()
