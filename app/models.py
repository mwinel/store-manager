import datetime


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


# Define class Product
class Product:
    """
    This class defines the product in terms of its
    id, name, description, quantity, price, category
    and date.
    """

    product_id = 1

    def __init__(self, name, description, quantity, price, category):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.category = category
        self.date = datetime.datetime.utcnow()
        self.id = Product.product_id
        Product.product_id += 1

    @property
    def serialize(self):
        """
        Returns product data in JSON serializable format.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category,
            "added on": self.date
        }

    def total_cost(self, quantity, price):
        return quantity * price


# Define sales class
class Sale:
    """
    This class defines a sales class.
    """

    sale_id = 1

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.date = datetime.datetime.utcnow()
        self.id = Sale.sale_id
        Sale.sale_id += 1

    @property
    def serialize(self):
        """
        Returns a sale order data in JSON serializable format.
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "total cost": self.quantity * self.price,
            "sold on": self.date
        }
