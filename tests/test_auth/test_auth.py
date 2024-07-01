from tests.exports.variables import ACCESS_TOKEN
from fastapi.testclient import TestClient
from src.main import app
import pytest

client = TestClient(app)


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_decode_token(client):
    # Mock a valid access token
    valid_token = ACCESS_TOKEN 
    # Test the decode token endpoint
    response = client.post("/auth/decode_token", json={"token": valid_token})
    assert response.status_code == 200
    data = response.json()
    assert "sub" in data
    assert "name" in data
