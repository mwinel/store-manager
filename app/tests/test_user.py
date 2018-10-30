from app.tests.base import BaseTestCase
from app.models import User


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
