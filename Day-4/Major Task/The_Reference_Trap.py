a = [1,2,3]

# Deep Copy - Copying the reference (memory address), not the data
b = a

b[0] = 99

print(a)

a1 = [1,2,3]

# Shallow Copy - Forcing Python to allocate a new list in memory
b1 = a1.copy()

print(b1)

