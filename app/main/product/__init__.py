from flask import Blueprint

api = Blueprint('product', __name__)

from app.main.product import views