# Global variable: currency rate for manufacturing cost calculations
currency_rate = 1.2  # USD to EUR exchange rate

# List of product names in the inventory
inventory = ["Widget A", "Widget B", "Widget C", "Widget D", "Widget E"]

# List of raw material costs per unit for various products
material_costs = [100, 250, 175, 300, 125]

# List of product prices
product_prices = [99.99, 150.00, 75.50, 199.99, 125.00]

# List of product quantities for production
product_quantities = [500, 1200, 750, 300, 900]

# List of product quality ratings (1-10 scale)
product_quality = [8, 7, 9, 6, 5, 10, 4]

# Dictionary with product details (id -> {name, price, stock})
products = {
    101: {"name": "Widget A", "price": 100, "stock": 500},
    102: {"name": "Widget B", "price": 150, "stock": 200},
    103: {"name": "Widget C", "price": 120, "stock": 0}
}

# 1. Get the number of products in the inventory using len()
num_products = len(inventory)
print(f"Total number of products in inventory: {num_products}")

# 2. Calculate the total material cost using sum()
total_material_cost = sum(material_costs)
print(f"Total material cost for manufacturing: {total_material_cost} EUR")

# 3. Find the minimum (cheapest) and maximum (most expensive) product prices using min() and max()
cheapest_product = min(product_prices)
most_expensive_product = max(product_prices)
print(f"Cheapest product price: {cheapest_product} EUR")
print(f"Most expensive product price: {most_expensive_product} EUR")

# 4. Sort the product quantities in ascending order using sorted()
sorted_quantities = sorted(product_quantities)
print(f"Sorted production quantities: {sorted_quantities}")

# 5. Check if all machines are ready (all() method) and if any machine is faulty (any() method)
machine_status = [True, True, False, True, True]
all_ready = all(machine_status)
any_faulty = any(not status for status in machine_status)
print(f"All machines ready: {all_ready}")
print(f"Any machine faulty: {any_faulty}")

# 6. Apply a 10% discount to all product prices using map()
def apply_discount(price):
    return price * 0.9  # 10% discount

discounted_prices = list(map(apply_discount, product_prices))
print(f"Discounted prices: {discounted_prices}")

# 7. Filter defective products based on their quality rating using filter()
def is_defective(rating):
    return rating < 6

defective_products = list(filter(is_defective, product_quality))
print(f"Defective product ratings: {defective_products}")

# 8. Access product stock safely using get()
product_id = 103
product_stock = products.get(product_id, {}).get('stock', 'Not Available')
print(f"Product stock for ID {product_id}: {product_stock}")

# 9. Round the total production cost to 2 decimal places using round()
labor_cost = 137.567
total_cost = round(labor_cost + total_material_cost, 2)
print(f"Total production cost: {total_cost} EUR")

# 10. Combine product names and quantities using zip()
combined = list(zip(inventory, product_quantities))
print("Product and Quantity Details:")
for product, quantity in combined:
    print(f"{product}: {quantity} units")

# 11. Get the manufacturing plant name (static variable)
manufacturing_plant = "Tech Industries Inc."
print(f"Manufacturing Plant: {manufacturing_plant}")

# 12. Get the number of products manufactured (class variable)
total_products_manufactured = sum(product_quantities)
print(f"Total products manufactured: {total_products_manufactured}")
