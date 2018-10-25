from flask import jsonify, request
from app.main.sale import api
from app.main.sale.sales import create_sales, get_all_sales
from app.main.auth.views import auth
from app.main.auth.admin import is_admin
from app.db import products


@api.route("/sales", methods=['POST'])
@auth.login_required
def add_sale():
    name = request.json.get('name')
    quantity = int(request.json.get('quantity'))
    price = int(request.json.get('price'))
    if name == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    product = [i for i in products if i.name == name]
    if not product:
        return jsonify({"message": "Product does not exist."}), 404
    return create_sales(name, quantity, price)


@api.route("/sales", methods=['GET'])
@auth.login_required
def get_sale_orders():
    if is_admin() is not True:
        return jsonify({"message": "Unauthorized Access!"}), 401
    return get_all_sales(), 200
