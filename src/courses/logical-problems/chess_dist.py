t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = (int(i) for i in input().split())
    res = max(abs(x1 - x2), abs(y1 - y2))
    print(res)
