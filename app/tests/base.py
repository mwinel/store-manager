import unittest
from manage import app
from app.main.errors.request_errors import RequestError
from app.models import User, Owner, Product


class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        self.app = app.test_client()
        self.request_error = RequestError()
        self.attendant = User("nelson", "nelson@example.com", "123456")
        self.owner = Owner("murungi", "murungi@example.com", "654321")
        self.product = Product("Tecno W3", "Tecno smart phone", "2", "$150",
                               "Mobile Phones")

        # Dummy attendants
        self.attendant1 = {
            "username": "sally",
            "email": "sally@example.com",
            "password": "123456"
        }

        self.attendant2 = {
            "username": " ",
            "email": "sally@example.com",
            "password": "123456"
        }

        self.attendant3 = {
            "username": "sally",
            "email": "sally@example.com",
            "password": "1234"
        }

        # Dummy owners
        self.owner1 = {
            "username": "paul",
            "email": "paul@example.com",
            "password": "123456"
        }

        self.owner2 = {
            "username": " ",
            "email": "paul@example.com",
            "password": "123456"
        }

        self.owner3 = {
            "username": "john",
            "email": "john@example.com",
            "password": "1234"
        }

        # Dummy products
        self.product1 = {
            "name": "Tecno W3",
            "description": "Mobile Smart Phone",
            "quantity": "3",
            "price": "$200",
            "category": "Mobile Phones"
        }

        self.product2 = {
            "name": " ",
            "description": "LCD 32 inch television",
            "quantity": "3",
            "price": "$600",
            "category": "Televisions"
        }

    def tearDown(self):
        pass
