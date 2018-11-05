import datetime
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.main.sale import api
from app.main.sale.sales import create_sale, get_all_sales
from app.main.product.products import get_product_by_id
from app.db import Database

db = Database()

@api.route("/sales", methods=['POST'])
@jwt_required # pragma: no cover
def add_sale():
    product_id = request.json.get("product_id")
    sale_quantity = request.json.get("sale_quantity")
    price = request.json.get("price")
    sale_date = datetime.datetime.now()
    if product_id <= 0 or sale_quantity <= 0:
        return jsonify({"message": "invalid input."}), 400
    product = get_product_by_id(product_id)
    inventory = product['quantity']
    if sale_quantity > inventory:
        return jsonify({"message": "not enough items in stock."}), 400
    if product:
        new_inventory = inventory - sale_quantity
        db.update_quantity(new_inventory, product_id)
        return create_sale(product_id, sale_quantity, price)
    else:
        return jsonify({"message": "product does not exist."}), 404

@api.route("/sales", methods=['GET'])
@jwt_required # pragma: no cover
def get_sales():
    return get_all_sales(), 200
