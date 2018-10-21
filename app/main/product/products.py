from flask import jsonify
from app.models import Product
from app.db import products


def create_product(name, description, quantity, price, category):
    """
    This method creates a new product.
    parameters: name, description, quantity, price, category.
    returns: a success message.
    """
    product = Product(name=name, description=description, quantity=quantity,
                      price=price, category=category)
    products.append(product)
    return jsonify({
        "message": "Product successfully added."
    }), 201


def get_all_products():
    """
    This method returns a list of all products.
    """
    return jsonify(Products=[i.serialize for i in products])


def get_product_by_name(name):
    """
    This method checks for a product given its title.
    parameters: title
    returns: True
    """
    for product in products:
        if product.name == name:
            return True
