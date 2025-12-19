import time

n = 1_000_000

numbers_list = list(range(1, n))
start = time.time()
-1 in numbers_list
end = time.time()
list_time = end - start

print(f"List lookup time: {list_time:.8f} seconds")

set_list = set(range(1, n))
start = time.time()
-1 in set_list
end = time.time()
set_time = end - start

print(f"Set lookup time: {set_time:.8f} seconds")

