# t = int(input())
# for _ in range(t):
#     n, a = int(input()), (int(i) for i in input().split())
#     a = sorted(a)
#     res = (i for x, y in zip(a[:n // 2], a[n // 2:][::-1]) for i in (x, y))
#     res = (*res, a[n // 2]) if n & 1 == 1 else res
#     print(*res)

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = []
    for i, e in enumerate(a):
        res.append(e)
        if len(res) > 1:
            swap = (i & 1 == 0 and res[-1] > res[-2]) or (i & 1 == 1 and res[-1] < res[-2])
            if swap:
                p1, p2 = res.pop(), res.pop()
                res.append(p1)
                res.append(p2)
    print(*res)
