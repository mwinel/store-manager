import re
import uuid
from flask import request, jsonify
from app.main.attendant import api
from app.main.auth.users import create_user, get_user_by_username
from app.models import User


@api.route("/signup", methods=['POST'])
def register_attendant():
    user_id = str(uuid.uuid4())
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    admin = False
    if username.strip() == "" or email.strip() == "" or password.strip() == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return jsonify({"message": "Username should not have spaces."}), 400
    if len(password) <= 5:
        return jsonify({"message": "Password too short."}), 400
    user_exists = get_user_by_username(username)
    if user_exists:
        return jsonify({"message": "User already exists."}), 400
    return create_user(user_id, username, email, password, admin)
