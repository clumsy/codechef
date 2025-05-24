t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    pp, p, res = float("-inf"), next(a), 1
    for i in a:
        if i < p:
            res -= 1 if i >= pp else 2
            if res < 0:
                break
        else:
            pp, p = p, i
    res = "YES" if res >= 0 else "NO"
    print(res)
