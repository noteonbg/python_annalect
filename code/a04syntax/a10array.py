# Define an array (list) of integers
arr = [10, 20, 30, 40, 50]

# 1. Adding an element to the array
arr.append(60)  # Adds 60 to the end of the array
print("After adding 60:", arr)

# 2. Modifying an element in the array
arr[2] = 35  # Changes the element at index 2 (third element) to 35
print("After modifying the element at index 2 to 35:", arr)

# 3. Finding an element in the array
element_to_find = 40
if element_to_find in arr:
    print(f"Element {element_to_find} found in the array at index {arr.index(element_to_find)}")
else:
    print(f"Element {element_to_find} not found in the array.")

# 4. Removing an element from the array
arr.remove(20)  # Removes the first occurrence of 20 from the array
print("After removing 20:", arr)

# 5. Printing all elements in the array
print("All elements in the array:")
for element in arr:
    print(element)
