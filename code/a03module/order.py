# order.py

def add_order(orders, product):
    orders.append(product)
    print(f"Ordered {product['name']}")

def total_cost(orders):
    return sum(product['price'] for product in orders) #coding style than performance..
