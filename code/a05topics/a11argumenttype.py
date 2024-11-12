from dataclasses import dataclass
from functools import reduce
from typing import List

# --- Step 1: Define the Product class as a Data Class ---
@dataclass
class Product:
    name: str
    base_cost: float
    labor_cost: float
    overhead_cost: float

    def total_cost(self) -> float:
        """Calculate the total cost of producing this product."""
        return self.base_cost + self.labor_cost + self.overhead_cost

    def __repr__(self):
        """Custom string representation for the Product object."""
        return f"{self.name} (Base: {self.base_cost}, Labor: {self.labor_cost}, Overhead: {self.overhead_cost})"

# --- Step 2: Create a list of products ---
products: List[Product] = [
    Product(name="Widget", base_cost=50.0, labor_cost=30.0, overhead_cost=20.0),
    Product(name="Gadget", base_cost=40.0, labor_cost=25.0, overhead_cost=15.0),
    Product(name="Doodad", base_cost=60.0, labor_cost=35.0, overhead_cost=25.0),
    Product(name="Thingamajig", base_cost=45.0, labor_cost=20.0, overhead_cost=18.0)
]

# --- Step 3: Use `map()` to calculate total cost for each product ---
def calculate_total_cost(product: Product) -> float:
    """Return the total cost of the product."""
    return product.total_cost()

# Use map to calculate the total costs for each product
total_costs = list(map(calculate_total_cost, products))

print("Total costs for each product:")
for product, total in zip(products, total_costs):
    print(f"{product.name}: {total}")

# --- Step 4: Use `reduce()` to calculate the total manufacturing cost ---
def add_costs(x: float, y: float) -> float:
    """Return the sum of two costs."""
    return x + y

# Use reduce to sum up the total costs of all products
total_manufacturing_cost = reduce(add_costs, total_costs)

print(f"\nTotal manufacturing cost for all products: {total_manufacturing_cost}")

# --- Step 5: Example of filtering and sorting products based on total cost ---

# Sort products by their total cost in ascending order
sorted_products_by_cost = sorted(products, key=lambda p: p.total_cost())
print("\nSorted products by total cost:")
for product in sorted_products_by_cost:
    print(f"{product.name}: {product.total_cost()}")

# Filter products with total cost greater than a certain threshold (e.g., 100)
threshold = 100
filtered_products = list(filter(lambda p: p.total_cost() > threshold, products))

print(f"\nProducts with total cost greater than {threshold}:")
for product in filtered_products:
    print(f"{product.name}: {product.total_cost()}")
