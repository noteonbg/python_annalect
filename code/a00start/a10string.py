def string_examples():
    # Creating strings
    greeting = "Hello"
    name = "Alice"
    
    # String concatenation
    full_greeting = greeting + ", " + name + "!"
    print("Concatenated String:", full_greeting)

    # String length
    print("Length of Full Greeting:", len(full_greeting))

    # Accessing characters in a string (indexing)
    first_char = full_greeting[0]
    print("First Character:", first_char)

    # Slicing a string
    sliced_string = full_greeting[7:12]  # Get 'Alice'
    print("Sliced String (7 to 12):", sliced_string)

    # Changing case
    print("Uppercase:", full_greeting.upper())
    print("Lowercase:", full_greeting.lower())

    # Checking for substrings
    print("Contains 'Alice'? :", 'Alice' in full_greeting)

    # String formatting
    age = 30
    formatted_string = f"{name} is {age} years old."
    print("Formatted String:", formatted_string)

    # Replacing parts of a string
    new_greeting = full_greeting.replace("Alice", "Bob")
    print("Replaced String:", new_greeting)

    # Splitting a string
    words = full_greeting.split(", ")
    print("Split String:", words)

    # Joining strings
    joined_string = " - ".join(words)
    print("Joined String:", joined_string)

if __name__ == "__main__":
    string_examples()
