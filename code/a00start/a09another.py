# product_management.py

def get_product_info(product_id):
    """Retrieve product information based on product ID."""
    # Sample product database (in practice, this could come from a database)
    products = {
        1: {"name": "Widget A", "price": 19.99, "quantity": 100},
        2: {"name": "Gadget B", "price": 29.99, "quantity": 50},
        3: {"name": "Widget C", "price": 24.99, "quantity": 0},
    }
    
    # Retrieve product info
    product = products.get(product_id)
    product["quantity"]=3;
    
    if product:
        return product["name"], product["price"], product["quantity"]
    else:
        return None, None, None  # Return None if the product is not found

def main():
    # Get product info for product ID 1
    product_name, product_price, product_quantity = get_product_info(1)

    if product_name:
        print(f"Product Name: {product_name}")
        print(f"Price: ${product_price:.2f}")
        print(f"Quantity in stock: {product_quantity}")
    else:
        print("Product not found.")

if __name__ == "__main__":
    main()


def calculate_rectangle_properties(length, width):
    #Calculate the area and perimeter of a rectangle.
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def main():
    # Example dimensions
    length = 5
    width = 3

    # Get the area and perimeter
    a, b = calculate_rectangle_properties(length, width)

    # Display the results
    print(f"Rectangle Length: {length}")
    print(f"Rectangle Width: {width}")
    print(f"Area: {a}")
    print(f"Perimeter: {b}")

if __name__ == "__main__":
    main()


"""
