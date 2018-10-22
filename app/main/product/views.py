from flask import jsonify, request
from app.main.product import api
from app.main.product.products import (create_product, get_product_by_name,
                                       get_all_products, get_product_by_id)
from app.main.auth.admin import is_admin
from app.main.auth.views import auth


@api.route("/products", methods=['POST'])
@auth.login_required
def add_product():
    name = request.json.get('name')
    description = request.json.get('description')
    quantity = request.json.get('quantity')
    price = request.json.get('price')
    category = request.json.get('category')
    if is_admin() is not True:
        return jsonify({"message": "Unauthorized Access!"}), 401
    if name == "" or description == "" or quantity == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if price == "" or quantity == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    already_exists = get_product_by_name(name)
    if already_exists:
        return jsonify({"message": "Product already exists."}), 400
    return create_product(name, description, quantity, price, category)


@api.route("/products", methods=['GET'])
@auth.login_required
def get_products():
    return get_all_products(), 200


@api.route("/products/<int:id>", methods=['GET'])
@auth.login_required
def get_product(id):
    return get_product_by_id(id)
