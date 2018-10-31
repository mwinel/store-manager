import json
from app.tests.base import BaseTestCase
from app.main.product.models import Product


class TestProductObject(BaseTestCase):
    """This class tests the product object."""

    def test_product_object(self):
        """Test whether an object is an instance of a class."""
        self.assertIsInstance(self.product, Product)

    def test_name(self):
        """Test name is an instance variable of a class."""
        self.assertEqual(self.product.name, "Tecno W3")

    def test_description(self):
        """Test description is an instance variable of a class."""
        self.assertEqual(self.product.description, "Tecno smart phone")

    def test_quantity(self):
        """Test quantity is an instance variable of a class."""
        self.assertEqual(self.product.quantity, "2")

    def test_price(self):
        """Test price is an instance variable of a class."""
        self.assertEqual(self.product.price, "$150")


class TestProductCase(BaseTestCase):
    """This class tests the products endpoints."""

    def test_create_product(self):
        """Test API can create a new product."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        rv = self.app.post("/api/v1/auth/admin/login",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 200)
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        b"Product successfully added." in rv.data

    def test_create_existing_product(self):
        """Test API can not create existing product."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Product already exists." in res.data

    def test_create_product_with_empty_fields(self):
        """Test API can not create a product with empty fields."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product2),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Fields cannot be left empty." in res.data

    def test_get_all_products(self):
        """Test API can fetch all products."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.get("/api/v1/products",
                           data=json.dumps(self.product2),
                           content_type='application/json')
        self.assertTrue(res.status_code, 200)

    def test_get_a_single_product(self):
        """Test API can fetch a single product."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.get("/api/v1/products/1",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(res.status_code, 200)

    def test_get_a_non_existing_product(self):
        """Test API can fetch a single product."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.get("/api/v1/products/1",
                           data=json.dumps(self.product2),
                           content_type='application/json')
        self.assertTrue(res.status_code, 404)
        b"Product does not exist." in res.data