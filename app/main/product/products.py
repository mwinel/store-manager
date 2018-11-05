from flask import jsonify
from app.main.product.models import Product
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

def update_a_product(name, description, quantity, price):
    """
    Updates a product.
    """
    product = Product(name=name, description=description, quantity=quantity,
                      price=price)
    db.update_product(name, description, quantity, price)
    return jsonify({"message": "product successfully updated."}), 201

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

def get_product_by_id(product_id):
    """
    Get product given its id.
    """
    product = db.get_by_argument('products', 'product_id', product_id)
    return product
