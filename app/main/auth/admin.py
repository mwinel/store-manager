from flask import jsonify
from app.models import Owner
from app.db import users


def create_store_owner(username, email, password):
    """
    Creates a new store owner.
    """
    owner = Owner(username=username, email=email, password=password)
    users.append(owner)
    return jsonify({"message": "Account successfully created."}), 201


def is_admin():
    """
    This method checks for the admin status.
    """
    for user in users:
        if user.admin is True:
            return True
