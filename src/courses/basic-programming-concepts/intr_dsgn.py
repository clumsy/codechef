t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = (int(i) for i in input().split())
    res = min(x1 + y1, x2 + y2)
    print(res)
