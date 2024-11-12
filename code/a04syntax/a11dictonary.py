# Define a dictionary with integer keys and string values
my_dict = {
    1: "Apple",
    2: "Banana",
    3: "Cherry"
}


# 1. Adding to a dictionary
my_dict[4] = "Date"  # Adds a new key-value pair: 4 -> "Date"
print("After adding a new key-value pair (4: 'Date'):", my_dict)

# 2. Viewing all elements in the dictionary
print("All elements in the dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# 3. Finding by a key
key_to_find = 3
if key_to_find in my_dict:
    print(f"Element with key {key_to_find} found: {key_to_find} -> {my_dict[key_to_find]}")
else:
    print(f"Element with key {key_to_find} not found.")

# 4. Getting all values
print("All values in the dictionary:")
values = my_dict.values()
for value in values:
    print(value)

# 5. Getting all keys
print("All keys in the dictionary:")
keys = my_dict.keys()
for key in keys:
    print(key)

# 6. Removing a key-value pair using `del`
key_to_remove = 2
if key_to_remove in my_dict:
    del my_dict[key_to_remove]  # Removes the key-value pair with key 2
    print(f"After removing key {key_to_remove}:", my_dict)
else:
    print(f"Key {key_to_remove} not found for removal.")

# 7. Removing a key-value pair using `pop()`
key_to_pop = 3
removed_value = my_dict.pop(key_to_pop, None)  # Removes key 3 and returns its value
if removed_value is not None:
    print(f"After popping key {key_to_pop}, removed value: '{removed_value}'")
else:
    print(f"Key {key_to_pop} not found for pop.")

# 8. Final state of the dictionary
print("Final state of the dictionary:")
print(my_dict)


my_dict = {'a': 1, 'b': 2, 'c': 3}

# Key to check and add if it doesn't exist
key_to_add = 'd'
value_to_add = 4

# Check if the key exists before adding
if key_to_add not in my_dict:
    my_dict[key_to_add] = value_to_add
    print(f"Key '{key_to_add}' added with value {value_to_add}.")
else:
    print(f"Key '{key_to_add}' already exists with value {my_dict[key_to_add]}.")

# Print the updated dictionary
print(my_dict)
