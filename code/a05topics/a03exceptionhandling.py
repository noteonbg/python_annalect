class MachineError(Exception):
    """Custom exception for machine errors (e.g., breakdowns, maintenance)."""
    pass

class InvalidOrderError(Exception):
    """Custom exception for invalid orders (e.g., missing parts, wrong order format)."""
    pass

class ProductionCapacityExceededError(Exception):
    """Custom exception for exceeding production capacity."""
    pass

class Machine:
    def __init__(self, name, status, capacity):
        self.name = name
        self.status = status  # "Operational", "Under Maintenance", etc.
        self.capacity = capacity  # Maximum production rate of the machine

    def start_production(self, order_quantity):
        """Start production on the machine."""
        if self.status != "Operational":
            raise MachineError(f"Machine '{self.name}' is not operational!")
        
        if order_quantity > self.capacity:
            raise ProductionCapacityExceededError(f"Order quantity {order_quantity} exceeds machine capacity {self.capacity}!")

        print(f"Production started on machine '{self.name}' for order quantity {order_quantity}.")

class ManufacturingOrder:
    def __init__(self, order_id, product_name, quantity, machine):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.machine = machine

    def validate_order(self):
        """Validate the order."""
        if self.quantity <= 0:
            raise InvalidOrderError(f"Invalid quantity {self.quantity} for order '{self.order_id}'!")
        print(f"Order '{self.order_id}' is valid.")

    def process_order(self):
        """Process the order on the assigned machine."""
        try:
            self.validate_order()
            self.machine.start_production(self.quantity)
            print(f"Order '{self.order_id}' for {self.product_name} processed successfully!")
        except InvalidOrderError as e:
            print(f"Order processing failed: {e}")
        except MachineError as e:
            print(f"Machine error: {e}")
        except ProductionCapacityExceededError as e:
            print(f"Order processing failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage:

# Create machines
machine_1 = Machine("Machine A", "Operational", 1000)
machine_2 = Machine("Machine B", "Under Maintenance", 800)

# Create orders
order_1 = ManufacturingOrder(order_id="ORD123", product_name="Product A", quantity=500, machine=machine_1)
order_2 = ManufacturingOrder(order_id="ORD124", product_name="Product B", quantity=1200, machine=machine_1)
order_3 = ManufacturingOrder(order_id="ORD125", product_name="Product C", quantity=200, machine=machine_2)
order_4 = ManufacturingOrder(order_id="ORD126", product_name="Product D", quantity=-50, machine=machine_1)

# Process the orders
order_1.process_order()  # This should succeed
order_2.process_order()  # This should fail due to exceeding capacity
order_3.process_order()  # This should fail due to machine being under maintenance
order_4.process_order()  # This should fail due to invalid quantity
