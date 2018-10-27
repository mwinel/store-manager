from flask import Blueprint

api = Blueprint('sales', __name__)

from app.main.sale import views
