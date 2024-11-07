# inventory.py

# Example list of products in inventory
inventory = [
    {"id": 1, "name": "Widget A", "price": 19.99, "quantity": 100},
    {"id": 2, "name": "Gadget B", "price": 29.99, "quantity": 50},
    {"id": 3, "name": "Widget C", "price": 24.99, "quantity": 0},
]

def check_product_availability(product_name):
    """Check if a product is in inventory."""
    for product in inventory:
        if product["name"] == product_name:
            return product["quantity"] > 0
    return False

def compare_products(product1, product2):
    """Compare two products."""
    return product1 is product2, product1 == product2

def main():
    # Check if a product is available
    product_to_check = "Widget A"
    if check_product_availability(product_to_check):
        print(f"{product_to_check} is available in inventory.")
    else:
        print(f"{product_to_check} is not available in inventory.")

    # Creating two product instances
    product1 = {"id": 1, "name": "Widget A", "price": 19.99}
    product2 = product1  # Reference to the same object
    product3 = {"id": 1, "name": "Widget A", "price": 19.99}  # A different object with the same values

    # Comparing products
    same_instance, same_value = compare_products(product1, product2)
    print(f"product1 is product2: {same_instance} (is operator)")
    print(f"product1 == product2: {same_value} (== operator)")

    same_instance, same_value = compare_products(product1, product3)
    print(f"product1 is product3: {same_instance} (is operator)")
    print(f"product1 == product3: {same_value} (== operator)")

if __name__ == "__main__":
    main()
