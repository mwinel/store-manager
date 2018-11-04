import unittest
import json
from manage import app
from app.errors import RequestError
from app.main.auth.models import User
from app.main.product.models import Product
from app.main.sale.models import Sale
from app.db import Database


class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        self.app = app.test_client()
        self.request_errors = RequestError()
        self.db = Database()
        self.admin = User("nelson", "nelson@example.com", "123456", True)
        self.product = Product("Tecno W3", "Tecno smart phone", "2", "$150")
        self.sale = Sale("Tecno W3", "2", "299")

        self.admin1 = {
            "username": "admin",
            "password": "admin"
        }

        self.attendant1 = {
            "username": "amy",
            "email": "amy@example.com",
            "password": "123456",
            "admin": False
        }

        self.attendant2 = {
            "username": "lisa",
            "email": "lisa@example.com",
            "password": "123456",
            "admin": False
        }

        self.attendant3 = {
            "username": "susan",
            "email": "susan@example.com",
            "password": "pis",
            "admin": False
        }

        self.attendant4 = {
            "email": "susan@example.com",
            "password": "123456",
            "admin": False
        }

        self.attendant5 = {
            "username": "susan",
            "password": "123456",
            "admin": False
        }

        self.attendant3 = {
            "username": "susan",
            "email": "susan@example.com",
            "admin": False
        }

        # Dummy products
        self.product1 = {
            "name": "Tecno W3",
            "description": "Mobile Smart Phone",
            "quantity": "3",
            "price": "200"
        }

        self.product2 = {
            "name": " ",
            "description": "LCD 32 inch television",
            "quantity": "3",
            "price": "600"
        }

        self.product3 = {
            "name": " ",
            "description": "LCD 32 inch television",
            "quantity": "3",
            "price": " "
        }

        self.product4 = {}

        self.product5 = {
            "description": "LCD 32 inch television",
            "quantity": "3",
            "price": " "
        }

        self.product6 = {
            "name": "Soap",
            "quantity": "3",
            "price": " "
        }

        self.product7 = {
            "name": "Salt",
            "description": "LCD 32 inch television",
            "price": "100"
        }

        self.product8 = {
            "name": "Ball",
            "description": "LCD 32 inch television",
            "quantity": "3",
        }


    def tearDown(self):
        pass
