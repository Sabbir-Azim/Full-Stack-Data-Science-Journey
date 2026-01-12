from functools import partial

def power(b,e): return b**e

square=partial(power,e=2)

print(square(5))