"""Unit tests for app/utils.py."""

from app.utils import (
    APP_NAME,
    APP_VERSION,
    build_status_payload,
    build_version_payload,
)


def test_build_status_payload_ok():
    result = build_status_payload("ok")
    assert result == {"status": "ok"}


def test_build_status_payload_custom():
    result = build_status_payload("degraded")
    assert result == {"status": "degraded"}


def test_build_version_payload():
    result = build_version_payload()
    assert result["app"] == APP_NAME
    assert result["version"] == APP_VERSION


def test_app_version_format():
    # Version must follow basic semver pattern (digits and dots)
    parts = APP_VERSION.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
