# main.py

from factory import produce_product, list_products
from order import add_order, total_cost

def main():
    # List to hold produced products
    products = []

    # Produce some products
    products.append(produce_product("Widget A", 19.99))
    products.append(produce_product("Widget B", 24.99))

    # List produced products
    print("\nProducts produced:")
    list_products(products)

    # List to hold orders
    orders = []

    # Create an order
    add_order(orders, products[0])  # Ordering Widget A
    add_order(orders, products[1])  # Ordering Widget B

    # Show total cost of the order
    print(f"\nTotal order cost: ${total_cost(orders):.2f}")

if __name__ == "__main__":
    main()
