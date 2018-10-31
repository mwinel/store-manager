from flask import jsonify
from app.models import Product
from app.db import Database

db = Database()

def create_product(name, description, quantity, price):
    """
    Creates a new product.
    """
    product = Product(name=name, description=description, quantity=quantity,
                      price=price)
    db.insert_product(name, description, quantity, price)
    return jsonify({"message": "product successfully added."}), 201

def get_all_products():
    """
    This method returns a list of all products.
    """
    products = db.get_all('products')
    return jsonify(Products=products)

def get_product_by_name(name):
    """
    Get product given its name.
    """
    product = db.get_by_argument('products', 'name', name)
    return product

def get_product(product_id):
    """
    Get product by its id.
    """
    product = db.get_by_argument('products', 'product_id', product_id)
    if not product:
        return jsonify({"message": "product does not exist."}), 404
    return jsonify(Product=product)
