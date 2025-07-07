t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = ma = 0
    for i in a:
        ma = max(ma, i)
        res += (i + x - 1) // x
    res = min(res, ma)
    print(res)
