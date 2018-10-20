from flask import jsonify
from app.models import User
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
