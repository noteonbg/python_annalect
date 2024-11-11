# Define a user-defined class representing a manufacturing item
class ManufacturingItem:
    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}, Cost: ${self.cost:.2f}"

# Create an empty map (dictionary) where keys are strings and values are ManufacturingItem objects
inventory_map = {}

# Function to add or update an item in the map
def add_or_update_item(part_number, name, quantity, cost):
    item = ManufacturingItem(name, quantity, cost)
    inventory_map[part_number] = item

# Adding some items to the map
add_or_update_item("A123", "Widget", 100, 2.50)
add_or_update_item("B456", "Gadget", 200, 5.75)
add_or_update_item("C789", "Doodad", 150, 3.00)

# Checking if a key exists before adding or updating
part_to_check = "A123"
if part_to_check not in inventory_map:
    print(f"Part {part_to_check} not found. Adding new part.")
    add_or_update_item(part_to_check, "NewWidget", 500, 3.25)
else:
    print(f"Part {part_to_check} found, updating the existing part.")
    inventory_map[part_to_check].quantity += 50  # For example, updating the quantity

# Iterating through the map using keys
print("\nInventory using keys:")
for part_number in inventory_map:
    print(f"{part_number}: {inventory_map[part_number]}")

# Iterating through the map using keys and values
print("\nInventory using keys and values:")
for part_number, item in inventory_map.items():
    print(f"Part Number: {part_number} -> {item}")

# Updating an existing item in the map
print("\nUpdating part B456:")
inventory_map["B456"].quantity += 100  # Adding 100 more Gadgets
inventory_map["B456"].cost = 6.00  # Updating cost to 6.00
print(inventory_map["B456"])

# Removing a part from the map
print("\nRemoving part C789:")
del inventory_map["C789"]

# Final map after removal
print("\nFinal Inventory:")
for part_number, item in inventory_map.items():
    print(f"Part Number: {part_number} -> {item}")
