def new_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@new_decorator
def new_func():
    print("Hello world!")

new_func()