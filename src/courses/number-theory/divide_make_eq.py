from math import gcd


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    g = gcd(*a)
    res = sum(i != g for i in a)
    print(res)
