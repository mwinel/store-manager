from app.tests.base import BaseTestCase
from app.models import User, Owner


class TestUserObject(BaseTestCase):
    """This class tests the user object."""

    def test_user_object(self):
        """Test whether an object is an instance of a class."""
        self.assertIsInstance(self.attendant, User)
        self.assertIsInstance(self.owner, Owner)

    def test_username(self):
        """Test username is an instance variable of a class."""
        self.assertEqual(self.attendant.username, "nelson")
        self.assertEqual(self.owner.username, "murungi")

    def test_email(self):
        """Test email is an instance variable of a class."""
        self.assertEqual(self.attendant.email, "nelson@example.com")
        self.assertEqual(self.owner.email, "murungi@example.com")

    def test_password(self):
        """Test password is an instance variable of a class."""
        self.assertEqual(self.attendant.password, "123456")
        self.assertEqual(self.owner.password, "654321")

    def test_user_status(self):
        """Test whether user status is admin or not."""
        self.assertEqual(self.attendant.admin, False)
        self.assertEqual(self.owner.admin, True)
