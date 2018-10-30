import re
from flask import request, jsonify
from app.main.auth import api
from app.main.auth.users import (create_store_owner, get_all_users, 
                                 get_user_by_username)


@api.route("/admin/signup", methods=['POST'])
def register_admin():
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
    return create_store_owner(username, email, password, admin)


@api.route("/users", methods=['GET'])
def get_users():
    return get_all_users(), 200
