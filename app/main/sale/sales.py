from flask import jsonify
from app.main.sale.models import Sale
from app.db import Database

db = Database()

def create_sale(product_id, sale_quantity, price):
    """
    Creates a new sale.
    """
    sale = Sale(product_id=product_id, sale_quantity=sale_quantity, price=price)
    db.insert_sale(product_id, sale_quantity, price)
    return jsonify({"message": "sale successfully added."}), 201

def get_all_sales():
    """
    This method returns a list of all sales.
    """
    sales = db.get_all('sales')
    return jsonify(Sales=sales)
