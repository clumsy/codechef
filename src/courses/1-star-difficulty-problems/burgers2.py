from bisect import bisect_left


t = int(input())
for _ in range(t):
    x, y, n, r = (int(i) for i in input().split())
    lo, hi = 0, r // y
    while lo < hi:
        mi = hi - (hi - lo) // 2
        if mi * y + (n - mi) * x > r:
            hi = mi - 1
        else:
            lo = mi
    lo = min(lo, n)
    res = (n - lo, lo) if lo * y + (n - lo) * x <= r else (-1,)
    print(*res)
