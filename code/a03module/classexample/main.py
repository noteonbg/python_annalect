# main.py

from factory import Factory
from order import Order

def main():
    # Create a factory
    factory = Factory("Widget Factory")

    # Produce some products
    factory.produce("Widget A", 19.99)
    factory.produce("Widget B", 24.99)

    #content + operation when we use data type
    

    # List produced products
    print("\nProducts produced:")
    for product in factory.list_products():
        print(product)

    # Create an order
    order = Order()
    order.add_order(factory.list_products()[0])  # Ordering Widget A
    order.add_order(factory.list_products()[1])  # Ordering Widget B

    # Show total cost of the order
    print(f"\nTotal order cost: Rs{order.total_cost():.2f}")

if __name__ == "__main__":
    main()
