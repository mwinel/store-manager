import unittest
from manage import app
from app.main.errors.request_errors import RequestError


class BaseTestCase(unittest.TestCase):
    """Tests base case."""

    def setUp(self):
        self.app = app.test_client()
        self.request_error = RequestError()

    def tearDown(self):
        pass
