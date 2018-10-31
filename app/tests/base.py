import unittest
from manage import app
from app.main.errors.request_errors import RequestError
from app.main.auth.models import User
from app.main.product.models import Product


class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        self.app = app.test_client()
        self.request_error = RequestError()
        self.admin = User("1", "nelson", "nelson@example.com", "123456", True)
        self.product = Product("Tecno W3", "Tecno smart phone", "2", "$150")

        # Dummy users
        self.admin1 = {
            "username": "sally",
            "email": "sally@example.com",
            "password": "123456",
            "admin": True
        }

        self.admin2 = {
            "username": "john",
            "email": "john@example.com",
            "password": "123456",
            "admin": True
        }

        self.admin3 = {
            "username": "amy",
            "email": "amy@example.com",
            "password": "",
            "admin": True
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
            "password": "",
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

    def tearDown(self):
        pass
