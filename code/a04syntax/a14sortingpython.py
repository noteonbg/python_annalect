# Step 1: Define a user-defined class `Product`
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    # String representation of the object to help display it clearly
    def __repr__(self):
        return f"Product({self.product_id}, '{self.product_name}', {self.price})"


# Step 2: Create a list of Product objects
products = [
    Product(101, 'Widget', 19.99),
    Product(102, 'Gadget', 25.99),
    Product(103, 'Doodad', 15.49),
    Product(104, 'Thingamajig', 12.99),
    Product(105, 'Whatsit', 22.49)
]

# Step 3: Sort the products by product_name (description) in ascending order
products_sorted_by_name = sorted(products, key=lambda p: p.product_name)

# Print the sorted list by product_name (ascending)
print("Products sorted by product name (ascending):")
for product in products_sorted_by_name:
    print(product)

# Step 4: Sort the products by product_name in descending order
products_sorted_by_name_desc = sorted(products, key=lambda p: p.product_name, reverse=True)

# Print the sorted list by product_name (descending)
print("\nProducts sorted by product name (descending):")
for product in products_sorted_by_name_desc:
    print(product)
