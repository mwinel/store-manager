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

    def test_create_product_with_empty_name_fields(self):
        """Test API can not create a product with empty fields."""
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product2),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Fields cannot be left empty." in res.data

    def test_create_product_with_empty_price_fields(self):
        """Test API can not create a product with empty fields."""
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product3),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Fields cannot be left empty." in res.data

    def test_create_product_with_no_name_field(self):
        """Test API can not create a product with no name field."""
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product5),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"name field missing." in res.data

    def test_create_product_with_no_description_field(self):
        """Test API can not create a product with no description field."""
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product6),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"description field missing." in res.data

    def test_create_product_with_no_quantity_field(self):
        """Test API can not create a product with no quantity field."""
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product7),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"quantity field missing." in res.data

    def test_create_product_with_no_price_field(self):
        """Test API can not create a product with no price field."""
        res = self.app.post("/api/v1/products",
                            data=json.dumps(self.product7),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"price field missing." in res.data

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

    def test_delete_a_product(self):
        """Test API can delete a product."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.delete("/api/v1/products/1",
                              data=json.dumps(self.product1),
                              content_type='application/json')
        self.assertTrue(res.status_code, 200)
        b"product successfully deleted." in res.data

    def test_delete_for_a_non_existing_product(self):
        """Test delete for a non existing product."""
        res = self.app.delete("/api/v1/products/40000",
                              data=json.dumps(self.product4),
                              content_type='application/json')
        self.assertTrue(res.status_code, 404)
        b"product does not exist.." in res.data

    def test_update_a_product(self):
        """Test update for a product."""
        rv = self.app.post("/api/v1/products",
                           data=json.dumps(self.product1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.put("/api/v1/products/1",
                           data=json.dumps({
                               "name": "Tecno XYZ"
                            }),
                           content_type='application/json')
        self.assertTrue(res.status_code, 201)
        b"product successfully updated" in res.data

    def test_update_a_non_existing_product(self):
        """Test update for a non existing product."""
        res = self.app.put("/api/v1/products/1000",
                           data=json.dumps({
                               "name": "Tecno XYZ"
                            }),
                           content_type='application/json')
        self.assertTrue(res.status_code, 404)
        b"product does not exist." in res.data

    def test_update_product_with_empty_name_fields(self):
        """Test API can not create a update with empty fields."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.product2),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Fields cannot be left empty." in res.data

    def test_update_product_with_empty_price_fields(self):
        """Test API can not update a product with empty fields."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.product3),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Fields cannot be left empty." in res.data

    def test_update_product_with_no_name_field(self):
        """Test API can not update a product with no name field."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.product5),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"name field missing." in res.data

    def test_update_product_with_no_description_field(self):
        """Test API can not update a product with no description field."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.product6),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"description field missing." in res.data

    def test_update_product_with_no_quantity_field(self):
        """Test API can not update a product with no quantity field."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.product7),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"quantity field missing." in res.data

    def test_update_product_with_no_price_field(self):
        """Test API can not update a product with no price field."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.product7),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"price field missing." in res.data
