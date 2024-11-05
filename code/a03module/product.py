# product.py

def create_product(name, price):
    return {"name": name, "price": price}

def get_product_info(product):
    return f"{product['name']} - ${product['price']:.2f}"
