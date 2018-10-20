import unittest
from manage import app
from app.main.errors.request_errors import RequestError
from app.models import User, Owner


class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        self.app = app.test_client()
        self.request_error = RequestError()
        self.attendant = User("nelson", "nelson@example.com", "123456")
        self.owner = Owner("murungi", "murungi@example.com", "654321")

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

    def tearDown(self):
        pass
