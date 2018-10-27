from flask import jsonify
from app.models import Sale
from app.db import sales


def create_sales(name, quantity, price):
    """
    Method to create a new sale.
    """
    sale_order = Sale(name=name, quantity=quantity, price=price)
    sales.append(sale_order)
    return jsonify({
        "message": "Sale order successfully added."
    }), 201


def get_all_sales():
    """
    This method returns a list of sales.
    """
    return jsonify(Sales=[i.serialize for i in sales])


def get_sale_by_id(id):
    """
    Checks for a sale order given its id.
    """
    sale = [i.serialize for i in sales if i.id == id]
    if not sale:
        return jsonify({"message": "Sale order does not exist."}), 404
    return jsonify(Sale=sale), 200
