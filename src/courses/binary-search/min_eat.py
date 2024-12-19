t = int(input())
for _ in range(t):
    n, h = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    lo, hi = 1, max(a)
    while lo < hi:
        mi = lo + (hi - lo) // 2
        if sum((i + mi - 1) // mi for i in a) <= h:
            hi = mi
        else:
            lo = mi + 1
    res = lo
    print(res)
