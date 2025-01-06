t = int(input())
for _ in range(t):
    n, x = int(input()), [int(i) for i in input().split()]
    x.sort()
    mi, ma = float("inf"), -float("inf")
    cur = 0
    for i, v in enumerate(x):
        if i and v - x[i - 1] > 2:
            mi = min(mi, cur)
            ma = max(ma, cur)
            cur = 0
        cur += 1
    mi = min(mi, cur)
    ma = max(ma, cur)
    res = mi, ma
    print(*res)
