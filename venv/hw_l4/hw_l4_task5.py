from functools import reduce

def multi(a, b):
    return a * b

print(reduce(multi, list(i for i in list(range(100, 1001)) if i % 2 == 0)))