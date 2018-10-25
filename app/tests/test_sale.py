import json
from app.tests.base import BaseTestCase
from app.models import Sale


class TestSaleObject(BaseTestCase):
    """This class tests the sale object."""

    def test_sale_object(self):
        """Test whether an object is an instance of a class."""
        self.assertIsInstance(self.sale, Sale)

    def test_name(self):
        """Test name is an instance variable of a class."""
        self.assertEqual(self.sale.name, "Sony LED TV")

    def test_quantity(self):
        """Test quantity is an instance variable of a class."""
        self.assertEqual(self.sale.quantity, "2")

    def test_price(self):
        """Test price is an instance variable of a class."""
        self.assertEqual(self.sale.price, "299")


class TestSaleCase(BaseTestCase):
    """This class tests sales endpoints."""

    def test_create_sale_order(self):
        """Test API can create a new sale order."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.owner1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        rv = self.app.post("/api/v1/auth/admin/login",
                           data=json.dumps(self.owner1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 200)
        rv = self.app.post("/api/v1/sales",
                           data=json.dumps(self.sale1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)

    def test_create_sale_with_empty_fields(self):
        """Test API can not create a sale with empty fields."""
        rv = self.app.post("/api/v1/sales",
                           data=json.dumps(self.sale2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/sales",
                            data=json.dumps(self.sale2),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Fields cannot be left empty." in res.data

    def test_get_all_sales(self):
        """Test API can fetch all sales."""
        rv = self.app.post("/api/v1/sales",
                           data=json.dumps(self.sale1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.get("/api/v1/sales",
                           data=json.dumps(self.sale1),
                           content_type='application/json')
        self.assertTrue(res.status_code, 200)

    def test_get_a_single_sale(self):
        """Test API can fetch a single sale."""
        rv = self.app.post("/api/v1/sale",
                           data=json.dumps(self.sale1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.get("/api/v1/sales/1",
                           data=json.dumps(self.sale1),
                           content_type='application/json')
        self.assertTrue(res.status_code, 200)

    def test_get_a_non_existing_sale_order(self):
        """Test API can fetch a single sale."""
        rv = self.app.post("/api/v1/sales",
                           data=json.dumps(self.sale1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.get("/api/v1/sales/1",
                           data=json.dumps(self.sale2),
                           content_type='application/json')
        self.assertTrue(res.status_code, 404)
        b"Sale order does not exist." in res.data
