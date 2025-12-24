import time

n = 50000

# Test append()
lst = []
start_time = time.time()
for i in range(n):
    lst.append(i)
end_time = time.time()
time_append = end_time - start_time

print(f"Total time for append: {time_append:.8f}")

# Test insert(0)
lst = []
start_time = time.time()
for i in range(n):
    lst.insert(0, i)
end_time = time.time()
time_insert = time.time() - start_time

print(f"Total time for insert: {time_insert:.8f}")