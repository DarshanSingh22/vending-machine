from product import Product

class Purchase:
    product: Product
    amount: int

    def __init__(self, product, amount):
        self.product = product
        self.amount = amount