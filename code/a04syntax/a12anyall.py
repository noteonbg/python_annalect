# List of product quantities in a manufacturing plant
product_quantities = [150, 200, 0, 500, 50, 100, 300]

# Threshold for checking product quantities
threshold = 100

# Using any() to check if any product has a quantity greater than the threshold
any_above_threshold = any(quantity > threshold for quantity in product_quantities)

# Using all() to check if all products have a quantity greater than the threshold
all_above_threshold = all(quantity > threshold for quantity in product_quantities)

# Output results
print(f"Any product has a quantity greater than {threshold}: {any_above_threshold}")
print(f"All products have a quantity greater than {threshold}: {all_above_threshold}")
