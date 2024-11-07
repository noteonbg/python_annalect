# Sample data: Production quantities for machines in a factory
production_quantities = [100, 250, 150, 400, 220, 300, 180, 0, 350, 275]

# 1. **For Loop**: To process each production quantity
print("1. Using 'for' loop to process production quantities:")
for quantity in production_quantities:
    print(f"Machine produced {quantity} items.")

# 2. **While Loop**: To process the list using an index (like a traditional loop)
print("\n2. Using 'while' loop to process production quantities:")
index = 0
while index < len(production_quantities):
    print(f"Machine {index + 1} produced {production_quantities[index]} items.")
    index += 1

# 3. **Break Statement**: To stop processing when a certain condition is met (e.g., when production is 0)
print("\n3. Using 'break' statement when production is 0:")
for quantity in production_quantities:
    if quantity == 0:
        print("Production stopped due to machine breakdown (0 production).")
        break  # Stop the loop when 0 production is encountered
    print(f"Machine produced {quantity} items.")

# 4. **Continue Statement**: To skip certain machines (e.g., skip machines with low production)
print("\n4. Using 'continue' statement to skip machines with low production:")
for quantity in production_quantities:
    if quantity < 150:
        print(f"Skipping machine with {quantity} items produced (too low).")
        continue  # Skip this iteration if production is below a threshold
    print(f"Machine produced {quantity} items.")

# 5. **Else in Loops**: To execute a block of code if the loop completes without a 'break' (when no machine has zero production)
print("\n5. Using 'else' after a loop to ensure no machine had 0 production:")
for quantity in production_quantities:
    if quantity == 0:
        print("Production stopped early.")
        break
else:
    print("All machines have produced items successfully (no machine had 0 production).")

# 6. **Nested Loops**: If we had production quantities over several shifts, for example
print("\n6. Using 'nested' loops to show production for multiple shifts (for each machine and shift):")
shifts = ["Shift 1", "Shift 2", "Shift 3"]
# Let's simulate production per shift for each machine (2D data)
shift_production = [
    [100, 120, 110],  # Machine 1
    [150, 160, 170],  # Machine 2
    [200, 220, 210],  # Machine 3
    [50, 60, 55],     # Machine 4
    [300, 290, 310],  # Machine 5
]

for machine_index, machine in enumerate(shift_production, 1):
    print(f"\nProduction details for Machine {machine_index}:")
    for shift_index, production in enumerate(machine):
        print(f"{shifts[shift_index]}: {production} items")
        
# 7. **For-Else Loop**: Demonstrating a for loop with an else block (runs after loop if no break)
print("\n7. Using 'for-else' loop to ensure no shift had zero production:")
for machine in shift_production:
    if 0 in machine:  # If any shift had 0 production
        print("Production for a machine was interrupted (zero production in one of the shifts).")
        break
else:
    print("No machine had zero production in any shift.")

"""
For Loop:

This loop iterates over each machine's production quantity in the production_quantities list and prints out the amount produced for each machine.
While Loop:

The while loop processes the list by manually managing the index. It continues iterating over the production_quantities list until it reaches the end.
Break Statement:

The loop will stop as soon as it encounters a production quantity of 0 (simulating a machine breakdown), and we break out of the loop early.
Continue Statement:

The continue statement skips over machines that produced fewer than 150 items, simulating the action of ignoring low-production machines.
Else with Loops:

The else block is executed only if the for loop completes normally (i.e., without encountering a break). This ensures that if all machines produced something (no 0 production), the message will be printed.
Nested Loops:

Here, we use a nested loop to simulate multiple shifts for each machine. The outer loop iterates over machines, and the inner loop iterates over the shifts for each machine. This allows us to process 2D data (production per shift for each machine).
For-Else Loop:

This is a combination of the for loop and the else block. If any machine's production in any shift is 0, the loop will break early, and the else block will not run. If no machine has 0 production in any shift, the else block is executed.

"""    
