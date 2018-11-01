import re
import uuid
from flask import request, jsonify
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (create_access_token, jwt_required,
                                get_jwt_identity)
from app.main.auth import api
from app.main.auth.users import (create_user, get_all_users, 
                                 get_user_by_username, get_user_by_status,
                                 check_user_password, is_admin)
from app.main.auth.models import User
from app.validators import Validation
from app.db import Database

validate = Validation()
db = Database()

@api.route("/admin/signup", methods=['POST'])
def register_admin():
    user_id = str(uuid.uuid4())
    username = request.json.get('username')
    email = request.json.get('email')
    password = User.hash_password(request.json.get('password'))
    admin = True
    validate_admin = validate.user_validation(username, email, password)
    if validate_admin:
        return jsonify({"message": validate_admin}), 400
    user_exists = get_user_by_username(username)
    if user_exists:
        return jsonify({"message": "user already exists."}), 400
    return create_user(user_id, username, email, password, admin)

@api.route("/signup", methods=['POST'])
@jwt_required
def register_attendant():
    admin = is_admin()
    if not admin:
        return jsonify({"message": "you cannot perform this function."}), 401
    user_id = str(uuid.uuid4())
    username = request.json.get('username')
    email = request.json.get('email')
    password = User.hash_password(request.json.get('password'))
    admin = False
    validate_attendant = validate.user_validation(username, email, password)
    if validate_attendant:
        return jsonify({"message": validate_attendant}), 400
    user_exists = get_user_by_username(username)
    if user_exists:
        return jsonify({"message": "user already exists."}), 400
    return create_user(user_id, username, email, password, admin)

@api.route("/admin/login", methods=['POST'])
@api.route("/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    current_user = get_user_by_username(username)
    user_password = check_user_password(password)
    if not current_user:
        return jsonify({"message": "Invalid credentials."}), 401
    if pbkdf2_sha256.verify(password, pbkdf2_sha256.hash(password)):
        access_token = create_access_token(identity=username)
        return jsonify({
            "message": "successfully logged in.",
            "access_token": access_token
        }), 200
    else:
        return jsonify({"message": "Invalid credentials."}), 401

@api.route("/users", methods=['GET'])
@jwt_required
def get_users():
    admin = is_admin()
    if admin:
        return get_all_users(), 200
    else:
        return jsonify({"message": "you cannot perform this function."}), 401
