"""Lists: Ordered, mutable, can hold mixed data types.
Tuples: Ordered, immutable, can hold mixed data types.
Dictionaries: Unordered, key-value pairs, mutable.
Sets: Unordered, unique elements, mutable.
Strings: Immutable sequence of characters.
Arrays: Efficient for storing homogeneous data types (from the array module).
Queues: FIFO data structure (from the queue module).
Stacks: LIFO data structure (using a list).
Deque: Double-ended queue, allows adding/removing from both ends (from collections module)."""

a = 100        # Integer
b = 3.14       # Float
c = "Hello"    # String
d = True       # Boolean

print(type(a), type(b), type(c), type(d))  # Shows the types of variables

# List: Can contain multiple items, including different data types
my_list = [1, 2, 3, "apple", 4.5, True]

print("List:", my_list)
print("First element:", my_list[0])   # Accessing the first element
print("Last element:", my_list[-1])   # Accessing the last element

# Modifying a list element
my_list[2] = "banana"
print("Modified list:", my_list)

# Adding an element to the list
my_list.append(100)
print("List after appending:", my_list)

# Removing an element from the list
my_list.remove("apple")
print("List after removing 'apple':", my_list)

# Tuple: Immutable sequence of values
my_tuple = (1, 2, 3, "apple", 4.5)

print("Tuple:", my_tuple)
print("Accessing an element:", my_tuple[2])

# Tuples cannot be changed, so attempting to modify will raise an error:
# my_tuple[1] = 100  # This would throw an error: 'tuple' object does not support item assignment

# Dictionary: Key-value pairs
my_dict = {
    "name": "Alice",
    "age": 25,
    "height": 5.7,
    "is_student": True
}

print("Dictionary:", my_dict)
print("Access value by key ('name'):", my_dict["name"])

# Modifying a dictionary
my_dict["age"] = 26
print("Modified dictionary:", my_dict)

# Adding a new key-value pair
my_dict["city"] = "New York"
print("Dictionary after adding a new key-value pair:", my_dict)

# Removing a key-value pair
del my_dict["is_student"]
print("Dictionary after deletion:", my_dict)

# Set: Unordered collection of unique elements
my_set = {1, 2, 3, 4, 5, 2, 3}  # Duplicate elements are automatically removed

print("Set:", my_set)

# Adding an element to a set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Set operations
another_set = {4, 5, 6, 7}
print("Union:", my_set | another_set)   # Union
print("Intersection:", my_set & another_set)   # Intersection


# String: A sequence of characters
my_string = "Hello, World!"

print("String:", my_string)
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# String slicing
print("Substring (characters 0 to 5):", my_string[:5])

# Strings are immutable
# my_string[0] = "h"  # This would raise an error

# String: A sequence of characters
my_string = "Hello, World!"

print("String:", my_string)
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# String slicing
print("Substring (characters 0 to 5):", my_string[:5])

# Strings are immutable
# my_string[0] = "h"  # This would raise an error

import queue

# Creating a FIFO queue
q = queue.Queue()

# Adding items to the queue
q.put(1)
q.put(2)
q.put(3)

print("Queue size:", q.qsize())

# Removing an item from the queue (FIFO)
print("Removed item:", q.get())
print("Queue after dequeue:", list(q.queue))  # Converting the queue to a list for visualization

# Stack: LIFO (Last-In-First-Out)
stack = []

# Pushing elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Popping an element from the stack
print("Popped element:", stack.pop())
print("Stack after popping:", stack)

from collections import deque

# Creating a deque
dq = deque([1, 2, 3, 4])

# Add to the right end
dq.append(5)

# Add to the left end
dq.appendleft(0)

print("Deque after additions:", dq)

# Remove from the right end
dq.pop()
print("Deque after pop:", dq)

# Remove from the left end
dq.popleft()
print("Deque after popleft:", dq)

