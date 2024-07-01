from fastapi.testclient import TestClient
from src.main import app
import pytest

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_read_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_read_server(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "The server is running as expected."}
