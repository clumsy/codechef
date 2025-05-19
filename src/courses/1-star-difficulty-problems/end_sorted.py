t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    f = l = 0
    for i, e in enumerate(a):
        if e == 1:
            f = i
        elif e == n:
            l = i
    res = f - 1 + n - 1 - (l - 1) - (f > l)
    print(res)
