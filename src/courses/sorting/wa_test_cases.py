t = int(input())
for _ in range(t):
    n = int(input())
    s = (int(i) for i in input().split())
    v = input()
    res = 100
    for si, vi in zip(s, v):
        if vi == "0":
            res = min(res, si)
    print(res)
