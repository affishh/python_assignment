def get_user_from_db(user_id):
    # Simulated DB call
    fake_db = {
        1: {"id": 1, "name": "Alice"},
        2: {"id": 2, "name": "Bob"},
        3: {"id": 3, "name": "Charlie"},
        4: {"id": 4, "name": "Diana"}
    }
    return fake_db.get(user_id)
