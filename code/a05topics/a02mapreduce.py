from functools import reduce

# Define a class representing a Product
class Product:
    def __init__(self, name, base_cost, labor_cost, overhead_cost):
        self.name = name
        self.base_cost = base_cost
        self.labor_cost = labor_cost
        self.overhead_cost = overhead_cost

    def __repr__(self):
        return f"{self.name} (Base: {self.base_cost}, Labor: {self.labor_cost}, Overhead: {self.overhead_cost})"

    def total_cost(self):
        """Calculate the total cost for the product."""
        return self.base_cost + self.labor_cost + self.overhead_cost

# List of products being manufactured
products = [
    Product("Product A", 50, 30, 20),
    Product("Product B", 40, 25, 15),
    Product("Product C", 60, 35, 25),
    Product("Product D", 45, 20, 18)
]

# --- Step 1: Use `map()` to calculate the total cost for each product ---
def calculate_total_cost(product):
    return product.total_cost()

# Apply map() to get the total cost of each product
total_costs = map(calculate_total_cost, products)

# Convert the result to a list and display
print("Total costs for each product:", list(total_costs))

# --- Step 2: Use `reduce()` to calculate the total manufacturing cost for all products ---
def add_costs(x, y):
    return x + y

# Apply reduce() to sum up the total costs for all products
total_manufacturing_cost = reduce(add_costs, map(calculate_total_cost, products))

print(f"Total manufacturing cost for all products: {total_manufacturing_cost}")
