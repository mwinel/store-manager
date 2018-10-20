import json
from app.tests.base import BaseTestCase


class TestAdminAuth(BaseTestCase):
    """This class tests the admin auth endpoints."""

    def test_create_store_owner(self):
        """Test API can signup new store owner."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.owner1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        b"Account successfully created." in rv.data

    def test_create_existing_store_owner(self):
        """Test API can not signup existing store owner."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.owner1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/admin/signup",
                            data=json.dumps(self.owner1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Store owner with username 'sally' already exists." in rv.data

    def test_signup_with_empty_username_field(self):
        """Test store owner can not signup with empty username field."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.owner2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Fields cannot be left empty." in rv.data

    def test_signup_with_short_password(self):
        """Test store owner can not signup with short password."""
        rv = self.app.post("/api/v1/auth/admin/signup",
                           data=json.dumps(self.owner3),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Password too short." in rv.data


class TestAttendantAuth(BaseTestCase):
    """This class tests the attendant auth endpoints."""

    def test_create_store_attendant(self):
        """Test API can signup new store attendant."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        b"Store attendant account successfully created." in rv.data

    def test_create_existing_store_attendant(self):
        """Test API can not signup existing store attendant."""
        rv = self.app.post("/api/v1/auth/signup",
                           data=json.dumps(self.attendant1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/v1/auth/admin/signup",
                            data=json.dumps(self.attendant1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Store attendant with username 'sally' already exists." in rv.data

    def test_signup_with_empty_username_field(self):
        """Test store attendant can not signup with empty username field."""
        rv = self.app.post("/api/v1/auth/signup",
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
