from functools import reduce

# Define a function that squares a number
def square(x):
    return x ** 2

# Define a function that adds two numbers
def add(x, y):
    return x + y

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to square each number in the list
squared_numbers = map(square, numbers)

# Use reduce() to sum up the squared numbers
total_sum = reduce(add, squared_numbers)

print(total_sum)  
