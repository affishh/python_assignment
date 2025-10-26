import pytest
from app.routes import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_existing_user(client):
    response = client.get("/user/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Alice"

def test_get_non_existing_user(client):
    response = client.get("/user/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"
