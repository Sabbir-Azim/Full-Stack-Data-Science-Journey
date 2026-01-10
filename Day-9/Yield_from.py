def first():
    yield 1
    yield 2
    yield 3

def second():
    yield 0
    yield from first()
    yield 3
    yield 4
    yield 5

for x in second():
    print(x)