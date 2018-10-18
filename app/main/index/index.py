from flask import jsonify
from app.main.index import api


@api.route("/index", methods=['GET'])
def index():
    return jsonify({"message": "Welcome to Store Manager."}), 200
