import sys

lst = [x for x in range(1_000_000)]
print(sys.getsizeof(lst))

gen = (x for x in range(1_000_000))
print(sys.getsizeof(gen))

