import json
from app import app

def test_get_users():
    client = app.test_client()
    response = client.get('/api/users')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert data[0]['name'] == 'Alice'

def test_add_user():
    client = app.test_client()
    new_user = {"id": 2, "name": "Bob"}
    response = client.post('/api/users', json=new_user)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['name'] == 'Bob'
