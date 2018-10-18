from app.tests.base import BaseTestCase


class TestIndex(BaseTestCase):
    """Test index api endpoint."""

    def test_index_api_endpoint(self):
        """Test index api endpoint."""
        rv = self.app.get('/api/v1/index')
        self.assertTrue(rv.status_code, 200)
        b"Welcome to Store Manager." in rv.data
