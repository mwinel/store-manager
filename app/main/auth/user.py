from flask import jsonify
from app.models import User, Owner
from app.db import users


def create_store_attendant(username, email, password):
    """
    This method creates a new store attendant.
    parameters: username, email, password.
    returns: a success message.
    """
    attendant = User(username=username, email=email, password=password)
    users.append(attendant)
    return jsonify({
        "message": "Store attendant account successfully created."
    }), 201


def create_store_owner(username, email, password):
    """
    This method creates a new store owner or admin.
    parameters: username, email, password.
    returns: a success message.
    """
    owner = Owner(username=username, email=email, password=password)
    users.append(owner)
    return jsonify({"message": "Account successfully created."}), 201


def get_all_users():
    """
    This method returns a list of all users.
    """
    return jsonify(Users=[i.serialize for i in users])


def get_user_by_username(username):
    """
    This method checks for a user given the username.
    parameters: username
    returns: True
    """
    for user in users:
        if user.username == username:
            return True
