t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    f = set(int(i) for i in input().split())
    c, a = [], []
    r = iter(range(1, n + 1))
    i = 0
    while r:
        v = next(r, None)
        if v is None:
            break
        if v not in f:
            (c if i == 0 else a).append(str(v))
            i = 1 - i
    res = " ".join(c or ["-1"]) + "\n" + " ".join(a or ["-1"])
    print(res)
