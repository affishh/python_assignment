# test_integration.py
import pytest
from app import app, db, User

@pytest.fixture
def client():
    # Create a clean test environment before each test
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # fresh DB
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        # Cleanup after test
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_add_and_get_user(client):
    # 1️⃣ Add a new user
    response = client.post('/api/users', json={'name': 'Alice'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Alice'

    # 2️⃣ Fetch all users
    response = client.get('/api/users')
    assert response.status_code == 200
    users = response.get_json()
    assert len(users) == 1
    assert users[0]['name'] == 'Alice'
