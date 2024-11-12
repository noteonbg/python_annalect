# Parent class (base class)
class Machine:
    def __init__(self, name, model, status="Operational"):
        self.name = name
        self.model = model
        self.status = status

    def start(self):
        """Simulate starting the machine."""
        print(f"Starting the {self.name} machine...")

    def stop(self):
        """Simulate stopping the machine."""
        print(f"Stopping the {self.name} machine...")

    def get_status(self):
        """Return the status of the machine."""
        return self.status

# Child class 1 (inherits from Machine)
class LatheMachine(Machine):
    def __init__(self, name, model, status="Operational", material="Steel"):
        super().__init__(name, model, status)  # Call the parent class's constructor
        self.material = material  # Specific attribute for LatheMachine

    def start(self):
        """Override the start method to add specific functionality."""
        print(f"Lathe machine {self.name} is now starting. Material: {self.material}")
        super().start()  # Call the parent class's start method

    def cut_material(self):
        """Specific method for LatheMachine."""
        print(f"Cutting material: {self.material} on the Lathe machine.")

# Child class 2 (inherits from Machine)
class DrillingMachine(Machine):
    def __init__(self, name, model, status="Operational", drill_type="Standard"):
        super().__init__(name, model, status)  # Call the parent class's constructor
        self.drill_type = drill_type  # Specific attribute for DrillingMachine

    def start(self):
        """Override the start method to add specific functionality."""
        print(f"Drilling machine {self.name} is now starting. Drill type: {self.drill_type}")
        super().start()  # Call the parent class's start method

    def drill_hole(self):
        """Specific method for DrillingMachine."""
        print(f"Drilling a hole with {self.drill_type} drill type.")

# Create instances of the child classes
lathe = LatheMachine(name="Lathe X1", model="LX100", material="Aluminum")
drill = DrillingMachine(name="Drill Z1", model="DZ200", drill_type="Hammer")

# Use methods from both parent and child classes
lathe.start()  # Will call the overridden start method in LatheMachine
lathe.cut_material()  # Calls a method specific to LatheMachine
print(f"Lathe status: {lathe.get_status()}")

drill.start()  # Will call the overridden start method in DrillingMachine
drill.drill_hole()  # Calls a method specific to DrillingMachine
print(f"Drill status: {drill.get_status()}")
