t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res = 0
    for i, e in enumerate(a):
        if e != 0:
            res = i
    print(res)
