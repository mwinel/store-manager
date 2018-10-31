from flask import jsonify, request
from app.main.product import api
from app.main.product.products import (create_product, get_product_by_name,
                                       get_all_products)
from app.db import Database

db = Database()

@api.route("/products", methods=['POST'])
def add_product():
    name = request.json.get('name')
    description = request.json.get('description')
    quantity = request.json.get('quantity')
    price = request.json.get('price')
    # if admin is not True:
    #     return jsonify({"message": "Unauthorized Access!"}), 401
    if name.strip() == "" or description.strip() == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if price.strip() == "" or quantity.strip() == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    already_exists = get_product_by_name(name)
    if already_exists:
        return jsonify({"message": "Product already exists."}), 400
    return create_product(name, description, quantity, price)

@api.route("/products", methods=['GET'])
def get_products():
    return get_all_products(), 200

@api.route("/products/<int:product_id>", methods=['GET'])
def fetch_product(product_id):
    product = db.get_by_argument('products', 'product_id', product_id)
    if product:
        return jsonify(Product=product), 200
    return jsonify({"message": "product does not exist."}), 404

@api.route("/products/<int:product_id>", methods=['DELETE'])
def delete_product(product_id):
    product = db.get_by_argument('products', 'product_id', product_id)
    if not product:
        return jsonify({"message": "product does not exist."}), 404
    db.delete_by_argument('products', 'product_id', product_id)
    return jsonify({"message": "product successfully deleted."}), 200
