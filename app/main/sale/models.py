# Define sale model
class Sale:
    """
    This class defines a sale in terms of the
    name, quantity and price.
    """

    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost
