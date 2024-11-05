import random

# Constants for production rates
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

# Variable to track quality checks
quality_pass_rate = 0.9

# Function to simulate production
def produce_products(hours):
    for hour in range(1, hours + 1):
        print(f"Hour {hour}:")
        for product, rate in production_rates.items():
            produced = rate  # number of products produced in one hour
            inventory[product] += produced
            print(f"Produced {produced} units of Product {product}. Current inventory: {inventory[product]}")

# Function to monitor inventory
def monitor_inventory(threshold):
    print("\nMonitoring inventory:")
    for product in inventory:
        if inventory[product] < threshold:
            print(f"Inventory of Product {product} is below threshold. Current inventory: {inventory[product]}")
            inventory[product] += 1  # simulate additional production
            print(f"Added 1 unit to Product {product}. Current inventory: {inventory[product]}")

# Function to perform quality checks
def quality_check():
    print("\nQuality check process:")
    quality_check_passed = {}
    for product in inventory:
        quality_check_passed[product] = []
        for item in range(inventory[product]):
            if random.random() < quality_pass_rate:
                quality_check_passed[product].append('Pass')
            else:
                quality_check_passed[product].append('Fail')
    return quality_check_passed

# Function to summarize quality check results
def summarize_quality_checks(quality_results):
    print("\nQuality check results:")
    for product, results in quality_results.items():
        passed = results.count('Pass')
        failed = results.count('Fail')
        print(f"Product {product}: Passed {passed}, Failed {failed}")

# Main function to run the manufacturing simulation
def run_manufacturing_simulation():
    total_hours = 8
    threshold = 30

    # Produce products
    produce_products(total_hours)

    # Monitor inventory
    monitor_inventory(threshold)

    # Perform quality checks
    quality_results = quality_check()

    # Summarize quality checks
    summarize_quality_checks(quality_results)

    # Final inventory summary
    print("\nFinal Inventory Summary:")
    for product, count in inventory.items():
        print(f"Product {product}: {count} units")

# Run the simulation
if __name__ == "__main__":
    run_manufacturing_simulation()

"""
run the script directly, it will execute the
 run_manufacturing_simulation() function, 
 which orchestrates the entire manufacturing simulation.
If this script were imported into another Python
 file, the simulation would not automatically run, preventing unwanted behavior and allowing the 
 importing script to use the functions
   defined in your code as needed.

"""    

"""
Variable Types:

Integers: Used for production_rates, inventory, total_hours, and threshold.
Floats: Used for quality_pass_rate to allow for decimal representation of the pass rate.
Strings: Used in keys of production_rates and inventory, as well as in print statements.
Lists: Used to store results of quality checks in quality_check_passed.
Dictionaries: Used for production_rates and inventory to associate product types with their respective values.
Decision-Making Structures:

If-Else Statements: Used in the monitor_inventory function to check if the inventory of each product is below the threshold.
Looping Structures: for loops are used for iterating over hours, products, and quality check results.
Functions:

produce_products(hours): Simulates the production process.
monitor_inventory(threshold): Checks and updates inventory based on a threshold.
quality_check(): Simulates quality checks for produced items.
summarize_quality_checks(quality_results): Summarizes the results of the quality checks.
run_manufacturing_simulation(): Main function that orchestrates the simulation flow.

"""


