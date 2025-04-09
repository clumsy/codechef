t = int(input())
for _ in range(t):
    n = int(input())
    lo, hi = 1, n
    while lo < hi:
        mi = lo + (hi - lo) // 2
        if mi * mi < n:
            lo = mi + 1
        else:
            hi = mi
    res = lo if lo * lo <= n else lo - 1
    print(res)
