from flask import jsonify
from app.models import User
from app.db import users


def create_store_attendant(username, email, password):
    """
    Create store attendant.
    """
    attendant = User(username=username, email=email, password=password)
    users.append(attendant)
    return jsonify({
        "message": "Store attendant account successfully created."
    }), 201
