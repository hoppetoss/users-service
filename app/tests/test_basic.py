"""Basic health endpoint tests."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz():
    """Test liveness probe endpoint."""
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz():
    """Test readiness probe endpoint."""
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


@pytest.mark.parametrize(
    "endpoint,expected_status",
    [
        ("/healthz", "ok"),
        ("/readyz", "ready"),
    ],
)
def test_health_endpoints_parametrized(endpoint: str, expected_status: str):
    """Test health endpoints using parametrization."""
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.json()["status"] == expected_status


def test_docs_available():
    """Test that API documentation is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
