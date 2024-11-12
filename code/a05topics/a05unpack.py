# --- Tuple Unpacking Example ---
# Tuple with a string and an integer
product_info = ("Widget", 25)  # product name and product price

# Unpacking the tuple into variables
product_name, product_price = product_info

# Output the unpacked values
print("Tuple Unpacking:")
print("Product Name:", product_name)
print("Product Price:", product_price)
print()

# --- Dictionary Unpacking Example ---
# Dictionary with product name and price
product_dict = {"product_name": "Gadget", "product_price": 30}

# Unpacking the dictionary using keys
product_name = product_dict["product_name"]
product_price = product_dict["product_price"]

# Output the unpacked values
print("Dictionary Unpacking:")
print("Product Name:", product_name)
print("Product Price:", product_price)
print()

# --- Dictionary Unpacking Using ** Operator ---
def display_product_info(product_details):
    # Function that unpacks dictionary using ** to access product details
    
    print(f"Product Name: {product_details['product_name']}")
    print(f"Product Price: {product_details['product_price']}")
    print()

# Dictionary to be unpacked
product_dict = {"product_name": "Doodad", "product_price": 45}


display_product_info(product_dict)

# --- Tuple Unpacking with zip() Example ---
# Two lists: product names and prices
product_names = ["Widget", "Gadget", "Doodad"]
product_prices = [25, 30, 45]

# Using zip to combine them into a list of tuples
product_info = zip(product_names, product_prices)

# Unpacking each tuple in the list of tuples
print("Tuple Unpacking with zip():")
for name, price in product_info:
    print(f"Product Name: {name}, Product Price: {price}")
