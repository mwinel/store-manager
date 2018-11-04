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

    def create_tables(self):
        """Creates all database tables."""
        with open('app/schema.sql') as tables:
            self.cursor.execute(tables.read())

    def insert_user_data(self, *args):
        """Insert user data into the database."""
        username = args[0]
        email = args[1]
        password = args[2]
        admin = args[3]
        user_query = "INSERT INTO users (username, email, password, admin)\
                      VALUES ('{}', '{}', '{}', '{}');".format(
                      username, email, password, admin)
        self.cursor.execute(user_query)

    def insert_product(self, *args):
        """Insert product data into the database."""
        name = args[0]
        description = args[1]
        quantity = args[2]
        price = args[3]
        product_query = "INSERT INTO products (name, description, quantity,\
                         price) VALUES ('{}', '{}', '{}', '{}');".format(
                         name, description, quantity, price)
        self.cursor.execute(product_query)

    def insert_sale(self, name, quantity, price):
        """Add sale to the database."""
        sale_query = "INSERT INTO sales (name, quantity, price)\
                      VALUES ('{}', '{}', '{}');".format(name, quantity, price)
        self.cursor.execute(sale_query)

    def update_quantity(self, quantity, product_id):
        """Update product quantity on sale."""
        query = "UPDATE products SET quantity = '{}'\
                 WHERE product_id = '{}'".format(quantity, product_id)
        self.cursor.execute(query)

    def update_product(self, *args):
        """Update product."""
        name = args[0]
        description = args[1]
        quantity = args[2]
        price = args[3]
        query = "UPDATE products SET name = '{}', description = '{}',\
                 quantity = '{}', price = '{}'".format(name, description, quantity, price)
        self.cursor.execute(query)
        row = self.cursor.rowcount
        if int(row) > 0:
            return True
        else:
            return False

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
        result = self.cursor.fetchone()
        return result

    def delete_by_argument(self, table, colum, argument):
        """Delete a record from the table"""
        query = "DELETE FROM {} WHERE {} = '{}'".format(
            table, colum, argument)
        self.cursor.execute(query)

    def drop_tables(self):
        """Drops database tables."""
        query = "DROP TABLE IF EXISTS {0} CASCADE"
        tables = ["users", "products", "sales", "complete"]
        for table in tables:
            self.cursor.execute(query.format(table))
