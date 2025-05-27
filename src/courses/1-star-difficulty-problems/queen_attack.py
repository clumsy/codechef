t = int(input())
for _ in range(t):
    n, x, y = (int(i) for i in input().split())
    res = min(x - 1, y - 1) + min(y - 1, n - x) + min(x - 1, n - y) + min(n - x, n - y) + 2 * (n - 1)
    print(res)
