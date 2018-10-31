import json
from app.tests.base import BaseTestCase
from app.main.auth.models import User


class TestUserObject(BaseTestCase):
    """This class tests the user object."""

    def test_user_object(self):
        """Test whether an object is an instance of a class."""
        self.assertIsInstance(self.admin, User)

    def test_username(self):
        """Test username is an instance variable of a class."""
        self.assertEqual(self.admin.username, "nelson")

    def test_email(self):
        """Test email is an instance variable of a class."""
        self.assertEqual(self.admin.email, "nelson@example.com")

    def test_password(self):
        """Test password is an instance variable of a class."""
        self.assertEqual(self.admin.password, "123456")


class TestAdminAuth(BaseTestCase):
    """This class tests the auth endpoints."""

    def test_create_store_admin(self):
        """Test API can signup new store admin."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        b"Account successfully created." in rv.data

    def test_create_existing_store_admin(self):
        """Test API can not signup existing store admin."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/admin/signup",
                            data=json.dumps(self.admin1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"User already exists." in rv.data

    def test_signup_with_empty_username_field(self):
        """Test store admin can not signup with empty username field."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Fields cannot be left empty." in rv.data

    def test_signup_with_short_password(self):
        """Test store admin can not signup with short password."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin3),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Password too short." in rv.data

    def test_store_admin_login(self):
        """Test API can login a store admin."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/admin/login",
                            data=json.dumps(self.admin1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 200)
        b"Successfully logged in." in res.data

    def test_store_admin_login_invalid_credentials(self):
        """Test API can not login store admin with invalid credentials."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/admin/login",
                            data=json.dumps({
                                "username": "paulo",
                                "password": "654321"
                            }),
                            content_type='application/json')
        self.assertTrue(res.status_code, 401)
        b"Invalid credentials." in res.data

    def test_login_for_non_registered_store_admin(self):
        """Test API can not login a non registered store admin."""
        rv = self.app.post("/api/v1/auth/admin/login",
                           data=json.dumps(self.admin1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 401)
        b"Invalid credentials." in rv.data


class TestAttendantAuth(BaseTestCase):
    """This class tests the attendants auth endpoints."""

    def test_create_store_attendant(self):
        """Test API can signup new store attendant."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        b"account successfully created." in rv.data

    def test_create_existing_store_attendant(self):
        """Test API can not signup existing store attendant."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/signup",
                            data=json.dumps(self.attendant1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"User already exists." in rv.data

    def test_signup_with_empty_username_field(self):
        """Test store attendant can not signup with empty username field."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.attendant2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Fields cannot be left empty." in rv.data

    def test_signup_with_short_password(self):
        """Test store attendant can not signup with short password."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant3),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Password too short." in rv.data

    def test_store_attendant_login(self):
        """Test API can login a store attendant."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/login",
                            data=json.dumps(self.attendant1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 200)
        b"Successfully logged in." in res.data

    def test_store_attendant_login_invalid_credentials(self):
        """Test API can not login store attendant with invalid credentials."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/login",
                            data=json.dumps({
                                "username": "paulo",
                                "password": "654321"
                            }),
                            content_type='application/json')
        self.assertTrue(res.status_code, 401)
        b"Invalid credentials." in res.data

    def test_login_for_non_registered_store_attendant(self):
        """Test API can not login a non registered store attendant."""
        rv = self.app.post("/api/v1/auth/login",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 401)
        b"Invalid credentials." in rv.data
