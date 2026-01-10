def large_file():
    for i in range(1_000_00):
        yield f"Line {i}"

for line in large_file():
    print(line)