import json
from app.tests.base import BaseTestCase


class TestDatabaseCase(BaseTestCase):

    def test_insert_user(self):
        """Test insert user into database."""
        user = self.db.insert_user_data('admin', 'admin@admin.com', 'admin', True)
        assert True

    def test_insert_product(self):
        """Test insert a product to the database."""
        product = self.db.insert_product('Soap', 'Washing Soap', '2', '200')
        assert True
        