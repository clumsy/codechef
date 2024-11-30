t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    res = 1 * min(x, y) + 2 * max(0, y - x)
    print(res)
