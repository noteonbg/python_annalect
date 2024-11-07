# Step 1: Define the user-defined class `Product`
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product({self.product_id}, '{self.product_name}', {self.price})"


# Step 2: Create a list of `Product` objects
products = [
    Product(101, 'Widget', 19.99),
    Product(102, 'Gadget', 25.99),
    Product(103, 'Doodad', 15.49),
    Product(104, 'Thingamajig', 12.99),
    Product(105, 'Whatsit', 22.49),
    Product(106, 'Wrench', 9.99)
]

# Step 3: Filter products based on price > 20
price_threshold = 20
filtered_by_price = filter(lambda p: p.price > price_threshold, products)

# Step 4: Filter products whose name contains 'Widget' (case-insensitive)
search_term = 'widget'
filtered_by_name = filter(lambda p: search_term.lower() in p.product_name.lower(), products)

# Step 5: Display the filtered results
print("Products with price greater than", price_threshold)
for product in filtered_by_price:
    print(product)

print("\nProducts with name containing the term:", search_term)
for product in filtered_by_name:
    print(product)
