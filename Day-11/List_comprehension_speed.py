import time

nums = list(range(1_000_000))

start = time.time()

result1 = list(map(lambda x: x*x, nums))

end = time.time()
print("map + lambda time:", end - start)

start = time.time()

result2 = [x*x for x in nums]

end = time.time()
print("list comprehension time:", end - start)
