def wrapper(func):
    def inner():
        print("Before the function")
        func()
        print("After the function")
    return inner

def func():
    print("Hello world!")

new_func = wrapper(func)
new_func()