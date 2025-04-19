t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = max(500 - 2 * x + 1000 - 4 * (x + y), 1000 - 4 * y + 500 - 2 * (x + y))
    print(res)
