list1 = [1, 2, 3, 6, 7, 8, 9, 10, 12, 15]
list2 = [4, 5, 6, 7, 9, 10]

duplicates = []

for i in list1:
    for j in list2:
        if i == j:
            duplicates.append(i)

print(duplicates)
