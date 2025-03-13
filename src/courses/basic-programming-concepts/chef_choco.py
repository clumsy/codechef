t = int(input())
for _ in range(t):
    c, x, y = (int(i) for i in input().split())
    res = max(0, (c - x) * y)
    print(res)
