"""


"""


# Example 1: Simple Lambda Function - Adding Two Numbers
def add(x,y):
    return x+y


add = lambda x, y: x + y  # 1. defn of function 2. we are assinging the function
result = add(5, 3) #who is calling the function we..
print(f"Add (5, 3): {result}")  # Output: 8

# Example 2: Lambda Function with One Argument - Squaring a Number
square = lambda x: x ** 2
print(f"Square of 4: {square(4)}")  # Output: 16




# Example 3: Lambda Function with No Arguments - Returning a Fixed Value
get_pi = lambda: 3.14159
print(f"Value of Pi: {get_pi()}")  # Output: 3.14159




# Example 4: Using Lambda with map() - Squaring a List of Numbers
numbers = [1, 2, 3, 4, 5] 
squared_numbers = map(lambda x: x ** 2, numbers)
print(f"Squared numbers: {list(squared_numbers)}")  # Output: [1, 4, 9, 16, 25]

# Example 5: Using Lambda with filter() - Filtering Even Numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Even numbers: {list(even_numbers)}")  # Output: [2, 4]

# Example 6: Using Lambda with sorted() - Sorting Products by Name

products = [{101: 'Widget'}, {102: 'Gadget'}, {103: 'Doodad'}]
sorted_products = sorted(products, key=lambda x: x[0])



print(f"Products sorted by name: {sorted_products}")
# Output: [(103, 'Doodad'), (102, 'Gadget'), (104, 'Thingamajig'), (101, 'Widget')]

# Example 7: Lambda Function with Multiple Arguments - Area of a Rectangle
area = lambda length, width: length * width
print(f"Area of rectangle (5, 3): {area(5, 3)}")  # Output: 15

# Example 8: Lambda with sorted() - Sorting Products by ID (Descending Order)
sorted_products_desc = sorted(products, key=lambda x: x[0], reverse=True)
print(f"Products sorted by ID (descending): {sorted_products_desc}")
# Output: [(104,
