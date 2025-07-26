t = int(input())
for _ in range(t):
    n = int(input())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    res = 0
    for r in range(n):
        cur = 0
        for k in range(0, n - r):
            cur = max(0, cur + a[r + k][k])
        res = max(res, cur)
    for c in range(1, n):
        cur = 0
        for k in range(0, n - c):
            cur = max(0, cur + a[k][c + k])
        res = max(res, cur)
    print(res)
