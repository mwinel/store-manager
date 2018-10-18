from flask import Blueprint

api = Blueprint('index', __name__)

from app.main.index import index
