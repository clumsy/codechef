from math import isqrt


t = int(input())
for _ in range(t):
    n, a = (int(i) for i in input().split())
    res = isqrt(n) * a
    print(res)
