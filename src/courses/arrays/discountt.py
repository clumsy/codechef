t = int(input())
for _ in range(t):
    n, x, y = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    d = 0
    for i in a:
        d += min(y, i)
    res = "COUPON" if d > x else "NO COUPON"
    print(res)
