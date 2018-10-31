from flask import jsonify
from app.main.sale import api


@api.route("/sales", methods=['POST'])
def add_sale():
    return jsonify({"message": "add a sale here coming soon..."})
