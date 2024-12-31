from math import gcd


t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = gcd(n, m)
    print(res)
