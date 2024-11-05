# main.py


from manufacturing import produce_product, list_products, add_order, total_order_cost, apply_discount

def main():
    # Lists to hold produced products and orders
    products = []
    orders = []

    # Produce some products
    produce_product(products, "Widget A", 19.99)
    produce_product(products, "Widget B", 24.99)
    produce_product(products, "Gadget C", 29.99)

    # List produced products
    list_products(products)

    # Apply a discount to all products
    apply_discount(products, 10)  # 10% discount

    # List products again to see the updated prices
    list_products(products)

    # Create some orders
    add_order(orders, products[0])  # Ordering Widget A
    add_order(orders, products[1])  # Ordering Widget B

    # List orders and show total cost
    print("\nOrders placed:")
    for order in orders:
        print(f"- {order['name']}: Rs {order['price']:.2f}")

    print(f"\nTotal order cost: Rs. {total_order_cost(orders):.2f}")

if __name__ == "__main__":
    main()
