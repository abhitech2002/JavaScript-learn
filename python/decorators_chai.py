import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} Time elapsed: {end - start}")
        return result
    return wrapper

@timer  
def my_decorator(n):
    time.sleep(n)

my_decorator(3)