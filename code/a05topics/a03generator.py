# Generator function that generates numbers up to a specified limit
def number_generator(limit):
    number = 0
    while number < limit:
        yield number
        
        number += 1

# Create a generator that produces numbers from 0 to 4
gen = number_generator(2)

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("no more values to generate")

# Iterate through the generator
"""
for num in gen:
    print(num)
"""

"""
The function number_generator(limit) generates numbers starting from 0 up to
 (but not including) the limit.
Each time yield is encountered, it returns the current number and pauses
 the execution of the function.
When the generator is resumed (using for or next()), the function
 continues executing from the point where it was paused.
 
 Lazy Evaluation: A generator "yields" values on demand and only computes the next value when requested, 
 which is helpful when dealing with large datasets.

"""


import time

# Generator to simulate real-time data stream
def sensor_data_stream():
    sensor_value = 0
    while True:
        yield sensor_value
        time.sleep(1)  # Simulate delay between sensor readings
        sensor_value += 1  # Simulate new sensor value

# Process the data stream
#data_gen = sensor_data_stream()

#for _ in range(10):
    #print(f"Sensor reading: {next(data_gen)}")

"""
# Generator to read a file line by line
def read_file_in_chunks(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk
"""
# Use the generator to process the file in chunks
#file_path = 'large_file.txt'
#for chunk in read_file_in_chunks(file_path):
 #  pass # process_chunk(chunk)  # Replace this with actual processing logic

