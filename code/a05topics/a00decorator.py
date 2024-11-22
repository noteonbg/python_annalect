def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed"

# Calling the decorated function
print(display())

#this is a decorator example i am showing you should tell this program is really not worth why?
#who created the decorator I
#who is using the decorator I.
#ok.. pathetic..

