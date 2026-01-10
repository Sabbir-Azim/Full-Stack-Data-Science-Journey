num = int(input("Write a number: "))

def square(n):
    yield n**2

def filter_even(gen):
    for n in gen:
        if n%2 != 0:
            yield n

x = filter_even(square(num))
print(next(x))



