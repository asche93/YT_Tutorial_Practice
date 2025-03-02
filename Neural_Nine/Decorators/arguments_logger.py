import functools


def logger(func):
    @functools.wraps(func)  # extracting meta data like name, docstrings
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}:")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@logger  # Decorator for function
def add(a, b):
    """Add two numbers"""
    return a + b


print(add.__name__)  # Output: Name of function "add"
print(add.__doc__)  # Output: Docstring summary "Add two numbers"

add(5, 7)  # Call like normal
