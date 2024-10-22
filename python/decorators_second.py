def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

    
@debug
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")

greet("John", greeting="Hi")