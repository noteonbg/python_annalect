# order.py

from product import Product
from factory import Factory

class Order:
    def __init__(self):
        self.orders = []

    def add_order(self, product):
        self.orders.append(product)
        print(f"Ordered {product}")

    def total_cost(self):
        return sum(product.price for product in self.orders)
