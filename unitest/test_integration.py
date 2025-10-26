import json
from app import app, users

def test_add_and_retrieve_user():
    client = app.test_client()
    new_user = {"id": 3, "name": "Charlie"}
    post_response = client.post('/api/users', json=new_user)
    assert post_response.status_code == 201

    get_response = client.get('/api/users')
    data = json.loads(get_response.data)
    assert any(u['name'] == 'Charlie' for u in data)
