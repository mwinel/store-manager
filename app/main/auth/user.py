from flask import jsonify
from app.db import Database


db = Database()


def get_all_users():
    """
    This method returns a list of all users.
    """
    users = db.fetch_users()
    return jsonify(Users=users)

