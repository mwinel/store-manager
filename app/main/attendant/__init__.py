from flask import Blueprint

api = Blueprint('attendant', __name__)

from app.main.attendant import views