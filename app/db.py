import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    """
    This class defines and holds all database queries.
    """

    def __init__(self):
        """Initialize database connection."""
        self.connection = psycopg2.connect(
            database="store_manager", user="murungi", password="myPassword", port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        print("connected yessssssss")

    def create_tables(self):
        """Creates all database tables."""
        create_user_table = "CREATE TABLE IF NOT EXISTS users\
        (user_id VARCHAR(50), username VARCHAR(20), \
        email VARCHAR(20), password VARCHAR(20), admin BOOLEAN DEFAULT FALSE);"
        self.cursor.execute(create_user_table)

        create_product_table = "CREATE TABLE IF NOT EXISTS products\
        (product_id SERIAL PRIMARY KEY, name VARCHAR(40), description VARCHAR(200),\
        quantity INTEGER, price INTEGER);"
        self.cursor.execute(create_product_table)

    def insert_user_data(self, *args):
        """Insert user data into the database."""
        user_id = args[0]
        username = args[1]
        email = args[2]
        password = args[3]
        admin = args[4]
        user_query = "INSERT INTO users (user_id, username, email, password, admin)\
        VALUES ('{}', '{}', '{}', '{}', '{}');".format(
            user_id, username, email, password, admin)
        self.cursor.execute(user_query)

    def insert_product(self, *args):
        """Insert product data into the database."""
        name = args[0]
        description = args[1]
        quantity = args[2]
        price = args[3]
        product_query = "INSERT INTO products (name, description, quantity,\
        price) VALUES ('{}', '{}', '{}', '{}');".format(name, description, quantity,
                                                        price)
        self.cursor.execute(product_query)

    def get_all(self, table):
        """Return all rows from a table."""
        query = "SELECT * FROM {};".format(table)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

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
        tables = ["users", "products"]
        for table in tables:
            self.cursor.execute(query.format(table))
