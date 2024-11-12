def repeat(num_times):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            for _ in range(num_times):
                print(f"Executing {original_function.__name__}...")
                result = original_function(*args, **kwargs)
            return result
        return wrapper_function
    return decorator_function

@repeat(num_times=3)
def say_hello(name):
    return f"Hello {name}"

# Calling the decorated function
print(say_hello("Alice"))
