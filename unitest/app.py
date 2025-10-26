# app.py
from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

users = [{"id": 1, "name": "Alice"}]

@app.route('/')
def home():
    return render_template_string("<h1>Welcome to the Sample App</h1>")

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
