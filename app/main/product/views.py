from flask import jsonify, request
from app.main.product import api
from app.main.product.products import (create_product, get_product_by_name,
                                       get_all_products, update_a_product)
from app.db import Database
from app.validators import Validation

db = Database()
validate = Validation()

@api.route("/products", methods=['POST'])
def add_product():
    name = request.json.get('name')
    description = request.json.get('description')
    quantity = request.json.get('quantity')
    price = request.json.get('price')
    validate_product = validate.product_validation(name, description,
                                                   quantity, price)
    if validate_product:
        return jsonify({"message": validate_product}), 400
    already_exists = get_product_by_name(name)
    if already_exists:
        return jsonify({"message": "Product already exists."}), 400
    return create_product(name, description, quantity, price)

@api.route("/products", methods=['GET'])
def get_products():
    return get_all_products(), 200

@api.route("/products/<int:product_id>", methods=['PUT'])
def edit_product(product_id):
    product = db.get_by_argument('products', 'product_id', product_id)
    if product:
        name = request.json.get('name')
        description = request.json.get('description')
        quantity = request.json.get('quantity')
        price = request.json.get('price')
        validate_update = validate.product_validation(name, description,
                                                      quantity, price)
        if validate_update:
            return jsonify({"message": validate_update}), 400
        already_exists = get_product_by_name(name)
        if already_exists:
            return jsonify({"message": "Product already exists."}), 400
        return update_a_product(name, description, quantity, price)
    else:
        return jsonify({"message": "product does not exist."}), 404

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
