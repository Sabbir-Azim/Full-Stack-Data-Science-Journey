def gen():
    yield 1
    yield 2
    yield 3

g = gen()

for _ in range(4):
    print(next(g))