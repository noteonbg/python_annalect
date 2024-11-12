import logging

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,  # Log all messages with severity level DEBUG or higher
    format='%(asctime)s - %(levelname)s - %(message)s',  # Custom log format
    handlers=[
        logging.StreamHandler(),  # Print log messages to console
        logging.FileHandler("machine_log.txt")  # Log messages to a file
    ]
)

class Machine:
    def __init__(self, name, model, status):
        self.name = name
        self.model = model
        self.status = status

    def __repr__(self):
        return f"Machine(name={self.name}, model={self.model}, status={self.status})"

    def update_status(self, new_status):
        """Method to update the machine's status and log the action."""
        old_status = self.status
        self.status = new_status
        logging.info(f"Machine '{self.name}' (ID: {id(self)}) status changed from '{old_status}' to '{new_status}'")

# Create a dictionary to store machines by their IDs
machines_dict = {
    101: Machine("Machine A", "M100", "Operational"),
    102: Machine("Machine B", "M200", "Under Maintenance"),
    103: Machine("Machine C", "M300", "Operational"),
}

# Log initial state of the machines
logging.info("Initial Machines in the system:")
for machine_id, machine in machines_dict.items():
    logging.info(f"Machine ID: {machine_id} -> {machine}")

# Example of modifying a machine's status and logging the event
logging.info("\nUpdating the status of Machine ID 102...")
machines_dict[102].update_status("Operational")

# Log the updated state of the machines
logging.info("\nUpdated Machines in the system:")
for machine_id, machine in machines_dict.items():
    logging.info(f"Machine ID: {machine_id} -> {machine}")

# Simulating an error or maintenance event
logging.error("Machine ID 101 is experiencing a critical failure and requires immediate attention.")
