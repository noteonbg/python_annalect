import asyncio

# An asynchronous function that simulates a task
async def task1():
    print("Task 1: Started")
    await asyncio.sleep(2)  # Simulate a 2-second task
    print("Task 1: Finished")

# Another asynchronous function that simulates a task
async def task2():
    print("Task 2: Started")
    await asyncio.sleep(1)  # Simulate a 1-second task
    print("Task 2: Finished")

# Main function that runs both tasks concurrently
async def main():
    # Create tasks and run them concurrently
    task1_task = asyncio.create_task(task1())
    #create a asyncjob and tell what is job it needs to run
    #return type is task object.. 

    task2_task = asyncio.create_task(task2())
    
    # Wait for both tasks to complete
    await task1_task
    await task2_task

# Run the main function
asyncio.run(main())
