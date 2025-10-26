from flask import Flask, jsonify, request
from app.db import get_user_from_db

app = Flask(__name__)

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_from_db(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404
