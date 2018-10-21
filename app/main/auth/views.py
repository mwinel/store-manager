import re
from flask import g, request, jsonify
from flask_httpauth import HTTPBasicAuth
from app.main.auth import api
from app.main.auth.attendant import create_store_attendant
from app.main.auth.admin import create_store_owner
from app.main.auth.user import get_all_users, get_user_by_username
from app.db import users


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = get_user_by_username(username)
    if not user:
        return False
    g.user = user
    return True


@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized Access!"}), 401


@api.route("/signup", methods=['POST'])
def user_signup():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if username == "" or email == "" or password == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return jsonify({"message": "Username should not have spaces."}), 400
    if len(password) <= 5:
        return jsonify({"message": "Password too short."}), 400
    attendant_exists = get_user_by_username(username)
    if attendant_exists:
        return jsonify({
            "message": "Store attendant with username '{}' already exists."
            .format(username)
        }), 400
    return create_store_attendant(username, email, password)


@api.route("/admin/signup", methods=['POST'])
def admin_signup():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if username == "" or email == "" or password == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return jsonify({"message": "Username should not have spaces."}), 400
    if len(password) <= 5:
        return jsonify({"message": "Password too short."}), 400
    owner_exists = get_user_by_username(username)
    if owner_exists:
        return jsonify({
            "message": "Store owner with username '{}' already exists."
            .format(username)
        }), 400
    return create_store_owner(username, email, password)


@api.route("/login", methods=['POST'])
@api.route("/admin/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    current_user = get_user_by_username(username)
    if not current_user:
        return jsonify({"message": "User does not exist."}), 404
    for user in users:
        if username == user.username and password == user.password:
            return jsonify({"message": "Successfully logged in."}), 200
        return jsonify({"message": "Invalid credentials."}), 400


@api.route("/users", methods=['GET'])
@auth.login_required
def get_users():
    return get_all_users(), 200
