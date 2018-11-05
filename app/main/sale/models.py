# Define sale model
class Sale:
    """
    This class defines a sale in terms of the
    name, quantity and price.
    """

    def __init__(self, product_id, sale_quantity, price):
        self.product_id = product_id
        self.sale_quantity = sale_quantity
        self.price = price
