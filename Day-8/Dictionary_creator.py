import time

lst = list(range(1_000_000))

# dict create time
start_time = time.time()
dictionary = {x: x for x in lst}
end_time = time.time()

create_time = end_time - start_time

print(f"Total time for Dictionary create: {create_time:.8f}")

# dict search time
start_time = time.time()
_ = 999_999 in dictionary
end_time = time.time()

search_time = end_time - start_time  

print(f"Total time for Dictionary search: {search_time:.8f}")


