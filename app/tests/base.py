import unittest
from manage import app
from app.main.errors.request_errors import RequestError
from app.models import User, Product, Sale


class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        self.app = app.test_client()
        self.request_error = RequestError()
        self.admin = User("nelson", "nelson@example.com", "123456", True)
        self.product = Product("Tecno W3", "Tecno smart phone", "2", "$150",
                               "Mobile Phones")
        self.sale = Sale("Sony LED TV", "2", "299")

        # Dummy attendants
        self.admin = {
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

    def tearDown(self):
        pass
