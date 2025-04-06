import operator
from functools import reduce

t = int(input())
for _ in range(t):
    n = int(input())
    res = reduce(operator.mul, range(1, n + 1))
    print(res)
