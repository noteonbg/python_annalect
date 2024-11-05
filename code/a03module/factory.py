# factory.py

from product import create_product, get_product_info

def produce_product(name, price):
    product = create_product(name, price)
    print(f"Produced {get_product_info(product)}")
    return product

def list_products(products):
    for product in products:
        print(get_product_info(product))
