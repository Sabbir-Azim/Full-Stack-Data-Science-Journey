def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function")
        func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 4))
