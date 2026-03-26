"""Shared utility helpers for the CI Release Platform service."""

APP_VERSION = "0.1.0"
APP_NAME = "ci-release-platform"


def build_status_payload(status: str) -> dict:
    """Return a standard status payload dict."""
    return {"status": status}


def build_version_payload() -> dict:
    """Return a standard version payload dict."""
    return {"app": APP_NAME, "version": APP_VERSION}
