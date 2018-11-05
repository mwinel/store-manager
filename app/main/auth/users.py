from flask import jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity
from app.main.auth.models import User
from app.db import Database

db = Database()

def is_admin():
    """Method to check user status."""
    current_user = get_jwt_identity()
    user = get_user_by_username(current_user)
    if user['admin'] == True:
        return True
    else:
        return False

def create_user(*args):
    """
    Creates a new store user.
    """
    user_id = args[0]
    username = args[1]
    email = args[2]
    password = args[3]
    admin = args[4]
    user = User(username=username, email=email,
                password=password, admin=admin)
    db.insert_user_data(username, email, password, admin)
    return jsonify({
        "message": "account successfully created."
    }), 201

def get_all_users():
    """
    This method returns a list of all users.
    """
    users = db.get_all('users')
    return jsonify(Users=users)

def get_user_by_username(username):
    """
    This method checks for a user given the username.
    """
    user = db.get_by_argument('users', 'username', username)
    return user

def get_user_by_status(admin):
    """
    This method returns a user given their admin status.
    """
    user = db.get_by_argument('users', 'admin', admin=True)
    return user

def check_user_password(password):
    """
    This method checks for the given password of a user."""
    user = db.get_by_argument('users', 'password', password)
    return user
