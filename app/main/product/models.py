# Define class Product
class Product:
    """
    This class defines the product in terms of its
    id, name, description, quantity, price.
    """

    def __init__(self, name, description, quantity, price):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
