import time

numbers = set(range(1, 10_000_001))

target = -5

start_time = time.time()

result = target in numbers

end_time = time.time()

total_time = end_time - start_time

print(f"Total time for set: {total_time:.8f}")