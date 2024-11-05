# manufacturing.py

def create_product(name, price):
    """Creates a product represented as a dictionary."""
    return {"name": name, "price": price}

def produce_product(products, name, price):
    """Produces a product and adds it to the products list."""
    product = create_product(name, price)
    products.append(product)
    print(f"Produced: {product['name']} at ${product['price']:.2f}")

def list_products(products):
    """Lists all produced products."""
    print("\nProducts produced:")
    for product in products:
        print(f"- {product['name']}: ${product['price']:.2f}")

def add_order(orders, product):
    """Adds a product to the order list."""
    orders.append(product)
    print(f"Ordered: {product['name']}")

def total_order_cost(orders):
    """Calculates the total cost of all orders."""
    return sum(product['price'] for product in orders)

def apply_discount(products, percentage):
    """Applies a discount to all products."""
    for product in products:
        original_price = product['price']
        discount_amount = original_price * (percentage / 100)
        product['price'] -= discount_amount
        print(f"Discount applied: {product['name']} from ${original_price:.2f} to ${product['price']:.2f}")
