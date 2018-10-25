from flask import jsonify
from app.models import Sale
from app.db import sales


def create_sales(name, quantity, price):
    """
    This method creates a new sale.
    returns: a success message.
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
