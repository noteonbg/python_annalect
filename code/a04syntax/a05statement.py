# Expression Statement (evaluates an expression)
a = 5 + 3    # Expression: a = 8
print(f"Expression result: {a}") 

# Assignment Statement
x = 10
y = x + 5    # Assign result of x + 5 to y
print(f"Value of y: {y}")

# Conditional (if-else) Statement
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Looping Statement (for loop)
print("\nFor loop demonstration:")
for i in range(3):  # Iterates over range(3) => 0, 1, 2
    print(f"Iteration {i}")

# Looping Statement (while loop)
print("\nWhile loop demonstration:")
i = 0
while i < 3:  # Loops while i is less than 3
    print(f"Iteration {i}")
    i += 1

# Break, Continue, and Pass Statements
print("\nBreak, Continue, Pass demonstration:")
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    if i == 4:
        break     # Exit the loop
    print(f"Current i: {i}")

# Function Definition Statement
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Calling the function

# Return Statement
def add(x, y):
    return x + y

sum_result = add(3, 4)
print(f"Sum result: {sum_result}")

# Import Statement
import math

# Using imported module
square_root = math.sqrt(16)
print(f"Square root of 16 is: {square_root}")

# Exception Handling (try-except) Statement
print("\nTry-except demonstration:")
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
else:
    print("Division was successful")
finally:
    print("This block always executes")

# Lambda (Anonymous Function) Statement
square = lambda x: x ** 2
print(f"Square of 5 is: {square(5)}")

# With Statement (Context Manager for file handling)
print("\nWith statement demonstration:")
# This block won't actually run since we are not working with a file in this environment,
# but here’s the syntax for using 'with' for file operations.
# with open("sample.txt", "w") as file:
#     file.write("Hello, world!")

# Global and Nonlocal Statements
x = 5  # Global variable

def modify_global():
    global x
    x = 20  # Modifies global variable 'x'

modify_global()
print(f"Modified global x: {x}")

# Nonlocal Statement
def outer():
    x = 10  # Variable in outer scope

    def inner():
        nonlocal x
        x = 20  # Modifies 'x' from the outer scope

    inner()
    print(f"Modified nonlocal x: {x}")

outer()

# Assertion Statement
assert 5 == 5  # This will pass
# assert 5 == 10  # Uncomment this to raise an AssertionError
"""
Expression Statement: a = 5 + 3 evaluates the expression 5 + 3 and assigns the result to a.
Assignment Statement: Assigns values to variables, like x = 10 and y = x + 5.
Conditional (if-else) Statement: Checks the value of x and prints corresponding messages.
Looping (for and while) Statements: Loops through numbers with both for and while loops.
Break, Continue, Pass: Demonstrates continue (skips the current iteration), break (exits the loop), and pass (does nothing, placeholder).
Function Definition: Defines the greet() function and calls it with a name.
Return Statement: A function add() returns the sum of two numbers.
Import Statement: Imports the math module and uses math.sqrt() to compute the square root.
Exception Handling: Uses a try-except block to handle potential errors (like division by zero).
Lambda Statement: Defines an anonymous function that squares a number.
With Statement: A context manager (normally used for file handling), though commented out in this code.
Global Statement: Demonstrates modifying a global variable using the global keyword.
Nonlocal Statement: Shows how nonlocal is used to modify a variable in the nearest enclosing scope.
Assertion Statement: Checks conditions and raises an AssertionError if the condition is False.
"""