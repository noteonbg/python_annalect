class Machine:
    def __init__(self, name, status, production_rate):
        self.name = name
        self.status = status
        self.production_rate = production_rate

    def __repr__(self):
        return f"Machine(name={self.name}, status={self.status}, production_rate={self.production_rate})"

# List of machines with integer keys (machine id) and values as Machine objects
machines = {
    101: Machine("Machine A", "Operational", 120.5),
    102: Machine("Machine B", "Under Maintenance", 95.0),
    103: Machine("Machine C", "Operational", 150.3),
    104: Machine("Machine D", "Operational", 110.0),
    105: Machine("Machine E", "Under Maintenance", 80.2)
}

# Convert the dictionary into a list of tuples (key, value) so we can sort by different criteria
machine_list = list(machines.items())

# --- Sorting by Various Criteria ---

# Sort by production rate (ascending)
sorted_by_production_rate = sorted(machine_list, key=lambda x: x[1].production_rate)
print("Sorted by Production Rate (Ascending):")
for key, machine in sorted_by_production_rate:
    print(f"Machine ID: {key}, {machine}")

# Sort by machine name (alphabetical order)
sorted_by_name = sorted(machine_list, key=lambda x: x[1].name)
print("\nSorted by Machine Name (Alphabetical):")
for key, machine in sorted_by_name:
    print(f"Machine ID: {key}, {machine}")

# Sort by status (Operational first), then by production rate (ascending)
sorted_by_status_and_production_rate = sorted(machine_list, key=lambda x: (x[1].status, x[1].production_rate))
print("\nSorted by Status and Production Rate:")
for key, machine in sorted_by_status_and_production_rate:
    print(f"Machine ID: {key}, {machine}")

# --- Filtering by Various Criteria using filter() ---

# Filter machines that are "Operational"
operational_machines = filter(lambda x: x[1].status == "Operational", machine_list)
print("\nOperational Machines:")
for key, machine in operational_machines:
    print(f"Machine ID: {key}, {machine}")

# Filter machines with production rate greater than 100
high_production_machines = filter(lambda x: x[1].production_rate > 100, machine_list)
print("\nMachines with Production Rate > 100:")
for key, machine in high_production_machines:
    print(f"Machine ID: {key}, {machine}")

# Filter machines that are "Under Maintenance"
maintenance_machines = filter(lambda x: x[1].status == "Under Maintenance", machine_list)
print("\nMachines Under Maintenance:")
for key, machine in maintenance_machines:
    print(f"Machine ID: {key}, {machine}")
