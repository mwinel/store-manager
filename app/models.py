# Define class User.
class User:
    """
    This class defines the user in terms of their
    id, username, email, password and role.
    """

    user_id = 1

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.admin = False
        self.id = User.user_id
        User.user_id += 1

    @property
    def serialize(self):
        """
        Returns user data in JSON serializable format.
        """
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "owner": self.admin
        }


# Define store owner or admin class.
class Owner(User):
    """
    This class defines the store owner by specifying
    their admin status.
    """

    def __init__(self, username, email, password):
        User.__init__(self, username, email, password)
        self.admin = True
