from flask import jsonify
from app.models import User
from app.db import Database

db = Database()

def create_user(user_id, username, email, password, admin):
    """
    Creates a new store owner.
    """
    user = User(user_id=user_id, username=username, email=email,
                password=password, admin=admin)
    db.insert_user_data(user_id, username, email, password, admin)
    return jsonify({"message": "account successfully created."}), 201

def get_all_users():
    """
    This method returns a list of all users.
    """
    users = db.fetch_users()
    return jsonify(Users=users)

def get_user_by_username(username):
    """
    This method checks for a user given the username.
    """
    user = db.get_by_argument('users', 'username', username)
    return user

def check_user_password(password):
    """
    This method checks for the given password of a user."""
    user = db.get_by_argument('users', 'password', password)
    return user
