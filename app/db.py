import psycopg2

class Database:
    """
    This class defines and holds all database queries.
    """

    def __init__(self):
        """Initialize database connection."""
        self.connection = psycopg2.connect(
            database="store_manager", port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        print("connected yessssssss")

    def create_tables(self):
        """Creates all database tables."""
        create_user_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id VARCHAR(50), username VARCHAR(20), \
        email VARCHAR(20), password VARCHAR(20), admin BOOLEAN DEFAULT FALSE);"
        self.cursor.execute(create_user_table)

    def insert_user_data(self, user_id, username, email, password, admin):
        """Insert user data into the database."""
        user_query = "INSERT INTO users (user_id, username, email, password, admin)\
        VALUES ('{}', '{}', '{}', '{}', '{}');".format(
            user_id, username, email, password, admin)
        self.cursor.execute(user_query)

    def fetch_users(self):
        """Fetch all users."""
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            row = {
                'user_id': row[0],
                'username': row[1],
                'email': row[2],
                'password': row[3],
                'admin': row[4]
            }
            users.append(row)
        return users

    def get_by_argument(self, table, column, argument):
        """Return a query by argument."""
        query = "SELECT * FROM {} WHERE {} = '{}';".format(
            table, column, argument)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def drop_tables(self):
        """Drops database tables."""
        query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users"]
        for table in tables:
            self.cursor.execute(query.format(table))
