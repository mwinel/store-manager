from flask import jsonify
from app.db import users


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
