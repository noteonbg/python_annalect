from datetime import date

# Step 1: Define the Product class
class Product:
    def __init__(self, name, price, manufacture_date):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
    
    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, manufacture_date={self.manufacture_date})"
    
# Step 2: Create a dictionary with product IDs (integers) as keys and Product objects as values
products_dict = {
    101: Product("Widget A", 20.5, date(2023, 5, 20)),
    102: Product("Widget B", 15.0, date(2023, 6, 15)),
    103: Product("Widget C", 25.0, date(2022, 12, 5)),
    104: Product("Widget D", 30.0, date(2024, 1, 10)),
}

# Step 3: Sorting the dictionary by keys (product IDs)

# Sort by keys (product IDs)
sorted_by_keys = dict(sorted(products_dict.items()))
print("Sorted by keys (product IDs):")
for key, product in sorted_by_keys.items():
    print(f"{key}: {product}")

# Step 4: Sorting the dictionary by values (e.g., by price or by manufacture date)

# Sort by product price (ascending)
sorted_by_price = dict(sorted(products_dict.items(), key=lambda item: item[1].price))
print("\nSorted by price:")
for key, product in sorted_by_price.items():
    print(f"{key}: {product}")

# Sort by manufacture_date (ascending)
sorted_by_date = dict(sorted(products_dict.items(), key=lambda item: item[1].manufacture_date))
print("\nSorted by manufacture date:")
for key, product in sorted_by_date.items():
    print(f"{key}: {product}")
