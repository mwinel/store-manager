import re
import uuid
from flask import request, jsonify
from app.main.auth import api
from app.main.auth.users import (create_user, get_all_users, 
                                 get_user_by_username, check_user_password)
from app.main.auth.models import User


@api.route("/admin/signup", methods=['POST'])
def register_admin():
    user_id = str(uuid.uuid4())
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    admin = True
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


@api.route("/admin/login", methods=['POST'])
@api.route("/login", methods=['POST'])
def login():
    usernname = request.json.get('username')
    password = request.json.get('password')
    current_user = get_user_by_username(usernname)
    user_password = check_user_password(password)
    if not current_user:
        return jsonify({"message": "Invalid credentials."}), 401
    if current_user and user_password:
        return jsonify({"message": "Successfully logged in."}), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401


@api.route("/users", methods=['GET'])
def get_users():
    return get_all_users(), 200
