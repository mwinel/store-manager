from passlib.hash import pbkdf2_sha256

# Define class User.
class User:
    """
    This class defines the user in terms of their
    id, username, email, password and role.
    """

    def __init__(self, user_id, username, email, password, admin):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.admin = False

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_password(password, hash):
        return pbkdf2_sha256(password, hash)
