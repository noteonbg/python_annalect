# Global variable: currency rate for manufacturing cost calculations
currency_rate = 1.2  # USD to EUR exchange rate

class Product:
    # Class variable: Total number of products manufactured in the plant
    total_products_manufactured = 0

    # Static variable: Manufacturing plant name, shared across all products
    manufacturing_plant = "Tech Industries Inc."

    def __init__(self, product_id, name, material_cost, labor_cost, quantity):
        # Instance variables: These belong to each instance (product)
        self.product_id = product_id
        self.name = name
        self.material_cost = material_cost
        self.labor_cost = labor_cost
        self.quantity = quantity

        # Increment the class variable to track total products manufactured
        Product.total_products_manufactured += quantity

    def calculate_total_cost(self):
        # Method to calculate the total cost for this product
        total_cost = (self.material_cost + self.labor_cost) * self.quantity
        return total_cost

    def get_product_details(self):
        # Method to return product details as a formatted string
        return f"Product ID: {self.product_id}\n" \
               f"Name: {self.name}\n" \
               f"Material Cost: {self.material_cost} EUR\n" \
               f"Labor Cost: {self.labor_cost} EUR\n" \
               f"Quantity: {self.quantity}\n" \
               f"Total Cost: {self.calculate_total_cost()} EUR"

    
    def get_total_products_manufactured(cls):
        # Class method to get the total number of products manufactured
        return Product.total_products_manufactured

    
    def get_manufacturing_plant():
        # Static method to get the manufacturing plant name
        return Product.manufacturing_plant

# Create product instances


print(f"\nTotal products manufactured: {Product.get_total_products_manufactured()}")
print(f"\nTotal products manufactured: {Product.get_manufacturing_plant()}")

"""
i=3
product1 = Product(product_id=101, name="Widget A", material_cost=50, labor_cost=30, quantity=100)
product2 = Product(product_id=102, name="Widget B", material_cost=60, labor_cost=35, quantity=200)


# Access instance variables and methods
print("Product 1 Details:")
print(product1.get_product_details())
print()
print("Product 2 Details:")
print(product2.get_product_details())

# Access class variable (total products manufactured)


# Access static variable (manufacturing plant name)
print(f"\nManufacturing Plant: {Product.get_manufacturing_plant()}")

# Access global variable (currency rate for cost conversion)
print(f"\nCurrency Rate (USD to EUR): {currency_rate}")
"""