def control_flow_example(numbers):
    print("Processing numbers:")
    
    for num in numbers:
        if num < 0:
            print(f"Skipping negative number: {num}")
            continue  # Skip the rest of the loop for negative numbers

        if num == 0:
            print("Encountered zero, stopping processing.")
            break  # Exit the loop if zero is encountered

        # A placeholder for future code; currently does nothing
        if num == 5:
            pass  # We can do nothing for 5 for now, but may add code later

        print(f"Processing number: {num}")

if __name__ == "__main__":
    # List of numbers to process
    numbers = [10, -2, 3, 5, 0, 8, -1, 7]
    control_flow_example(numbers)
