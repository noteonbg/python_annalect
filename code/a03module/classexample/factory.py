# factory.py

from product import Product

class Factory:
    def __init__(self, freak):
        self.name = freak
        self.products = []

    def f1(self):    
        print("f1 at work")

    def produce(self, product_name, price):
        product = Product(product_name, price)
        self.products.append(product)
        print(f"{self.name} produced {product}")

    def list_products(self):
        return self.products
