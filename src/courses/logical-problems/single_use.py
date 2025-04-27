t = int(input())
for _ in range(t):
    h, x, y = (int(i) for i in input().split())
    res = 1 + (0 if h <= y else (h - y + x - 1) // x)
    print(res)
