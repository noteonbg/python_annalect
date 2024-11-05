import timeit

def example_function():
    """Simulate a function that takes some time to execute."""
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

def measure_time_with_timeit():
    execution_time = timeit.timeit(example_function, number=10)  # Run the function 10 times
    print(f"Average Execution Time over 10 runs: {execution_time / 10:.6f} seconds")

if __name__ == "__main__":
    measure_time_with_timeit()

    """
    import time

def example_function():
    #Simulate a function that takes some time to execute.
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

def measure_time():
    start_time = time.time()  # Record the start time
    result = example_function()  # Call the function
    end_time = time.time()  # Record the end time

    execution_time = end_time - start_time  # Calculate the difference
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    measure_time()

    

    
    """
