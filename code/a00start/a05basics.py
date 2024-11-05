# List of products in inventory
products = ["Widget A", "Widget B", "Widget C"]
quantities = [100, 150, 200]  # Corresponding quantities for each product

# Function to display inventory
def display_inventory(products, quantities):
    print("Current Inventory:")
    for i in range(len(products)):
        print(f"{products[i]}: {quantities[i]} units")

# Function to update inventory
def update_inventory(product_name, quantity_change):
    if product_name in products:
        index = products.index(product_name)
        quantities[index] += quantity_change
        print(f"Updated {product_name}: {quantities[index]} units")
    else:
        print("Product not found.")

# Display initial inventory
display_inventory(products, quantities)

# Update inventory
update_inventory("Widget A", -10)  # Sold 10 units of Widget A
update_inventory("Widget B", 20)    # Received 20 more units of Widget B

# Display updated inventory
display_inventory(products, quantities)
