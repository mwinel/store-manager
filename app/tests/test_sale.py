import json
from app.tests.base import BaseTestCase
from app.main.sale.models import Sale


class TestSaleObject(BaseTestCase):
    """This class tests the sale object."""

    def test_sale_object(self):
        """Test whether an object is an instance of a class."""
        self.assertIsInstance(self.sale, Sale)

    # def test_name(self):
    #     """Test name is an instance variable of a class."""
    #     self.assertEqual(self.sale.name, "Tecno W3")

    def test_quantity(self):
        """Test quantity is an instance variable of a class."""
        self.assertEqual(self.sale.sale_quantity, "2")

    def test_price(self):
        """Test price is an instance variable of a class."""
        self.assertEqual(self.sale.price, "299")
