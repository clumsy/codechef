from itertools import product

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = (int(i) - 1 for i in input().split())
    res = "YES" if (x2 + y2) & 1 == (x1 + y1) & 1 else "NO"
    print(res)
