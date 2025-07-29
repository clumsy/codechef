import operator
from functools import reduce


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = all = reduce(operator.xor, a)
    for i in a:
        res = min(res, all ^ i)
    print(res)
