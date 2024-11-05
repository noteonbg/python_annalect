# Constants for production rates
import random

production_rates = {
    'A': 5,  # products per hour
    'B': 3,
    'C': 4
}

# Initial inventory
inventory = {
    'A': 0,
    'B': 0,
    'C': 0
}

# Total hours of production
total_hours = 8

# For loop to simulate production over a fixed number of hours
for hour in range(1, total_hours + 1):
    print(f"Hour {hour}:")
    for product, rate in production_rates.items():
        produced = rate  # number of products produced in one hour
        inventory[product] += produced
        print(f"Produced {produced} units of Product {product}. Current inventory: {inventory[product]}")

# While loop to monitor inventory and stop production if any product exceeds a threshold
threshold = 30
print("\nMonitoring inventory:")
while any(value < threshold for value in inventory.values()):
    for product in inventory:
        inventory[product] += 1  # simulate additional production
        print(f"Added 1 unit to Product {product}. Current inventory: {inventory[product]}")

# Nested loop to perform quality checks on the produced items
print("\nQuality check process:")
quality_check_passed = {}
for product in inventory:
    quality_check_passed[product] = []
    for item in range(inventory[product]):
        # Simulating a quality check (let's assume a 90% pass rate)
        if random.random() < 0.9:
            quality_check_passed[product].append('Pass')
        else:
            quality_check_passed[product].append('Fail')

# Summary of quality checks
print("\nQuality check results:")
for product, results in quality_check_passed.items():
    passed = results.count('Pass')
    failed = results.count('Fail')
    print(f"Product {product}: Passed {passed}, Failed {failed}")

# Final inventory summary
print("\nFinal Inventory Summary:")
for product, count in inventory.items():
    print(f"Product {product}: {count} units")
