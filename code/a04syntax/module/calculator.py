# calculator.py

"""
Modules help break the program into smaller, reusable components, making the code cleaner and more maintainable.
import allows you to include an entire module in your script, while from ... import allows you to bring specific functions directly into your script.
"""

import math_operations  # Import the math_operations module

# Define a few numbers to operate on
num1 = 15
num2 = 3

# Perform addition
result_add = math_operations.add(num1, num2)
print(f"{num1} + {num2} = {result_add}")

# Perform subtraction
result_subtract = math_operations.subtract(num1, num2)
print(f"{num1} - {num2} = {result_subtract}")

# Perform multiplication
result_multiply = math_operations.multiply(num1, num2)
print(f"{num1} * {num2} = {result_multiply}")

# Perform division
try:
    result_divide = math_operations.divide(num1, num2)
    print(f"{num1} / {num2} = {result_divide}")
except ValueError as e:
    print(e)
