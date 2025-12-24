import time

n = 50000

# Test pop()
lst = list(range(n))
start_time = time.time()
for i in range(n):
    lst.pop()
end_time = time.time()
time_append = end_time - start_time

print(f"Total time for pop(): {time_append:.8f}")

# Test pop(0)
lst = list(range(n))
start_time = time.time()
for i in range(n):
    lst.pop(0)
end_time = time.time()
time_insert = time.time() - start_time

print(f"Total time for pop(0): {time_insert:.8f}")