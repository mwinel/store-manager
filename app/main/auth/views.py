import re
from flask import request, jsonify
from app.main.auth import api
from app.main.auth.user import (create_store_attendant, create_store_owner,
                                get_all_users, get_user_by_username)


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


@api.route("/users", methods=['GET'])
def get_users():
    return get_all_users(), 200
