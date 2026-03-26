"""API integration tests using FastAPI TestClient."""

from fastapi.testclient import TestClient
from app.main import app
from app.utils import APP_NAME, APP_VERSION

client = TestClient(app)


def test_health_returns_200():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_ok_status():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_version_returns_200():
    response = client.get("/version")
    assert response.status_code == 200


def test_version_returns_correct_payload():
    response = client.get("/version")
    data = response.json()
    assert data["app"] == APP_NAME
    assert data["version"] == APP_VERSION


def test_unknown_route_returns_404():
    response = client.get("/nonexistent")
    assert response.status_code == 404
