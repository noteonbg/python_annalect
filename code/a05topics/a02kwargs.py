class Machine:
    def __init__(self, name, status="Operational"):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"Machine(name={self.name}, status={self.status})"

# Function to update the status of multiple machines using *args
def update_machines_status(*machines, new_status):
    for machine in machines:
        machine.status = new_status
        print(f"{machine.name} status updated to {new_status}")

# Function to update specific attributes of a machine using **kwargs
def update_machine_details(machine, **details):
    for key, value in details.items():
        if hasattr(machine, key):
            setattr(machine, key, value)
            print(f"Updated {key} of {machine.name} to {value}")
        else:
            print(f"{machine.name} does not have an attribute '{key}'.")

# Create machine objects
machine1 = Machine("Machine A")
machine2 = Machine("Machine B", "Under Maintenance")
machine3 = Machine("Machine C")

# Update status of multiple machines using *args
update_machines_status(machine1, machine2, machine3, new_status="Operational")

# Update specific attributes of a single machine using **kwargs
update_machine_details(machine1, status="Under Maintenance", name="Updated Machine A")
update_machine_details(machine2, status="Operational")
