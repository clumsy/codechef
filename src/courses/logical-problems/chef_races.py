t = int(input())
for _ in range(t):
    x, y, a, b = (int(i) for i in input().split())
    res = len({x, y} - {a, b})
    print(res)
