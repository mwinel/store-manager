from app.tests.base import BaseTestCase
from app.errors import RequestError


class TestRequestError(BaseTestCase):
    """Test the request error object."""

    def test_request_error_object(self):
        """Test whether an object is an instance of the RequestError class."""
        self.assertIsInstance(self.request_errors, RequestError)

    def test_not_found_error(self):
        """Test not found error response."""
        self.assertTrue(self.request_errors.not_found)
        rv = self.app.get("/api/v1/other")
        self.assertTrue(rv.status_code, 404)

    def test_method_not_allowed_error(self):
        """Test method not allowed error response."""
        self.assertTrue(self.request_errors.method_not_allowed)
        rv = self.app.put("/api/v1/products")
        self.assertTrue(rv.status_code, 405)
