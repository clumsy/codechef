t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = []
    for i in a:
        if not res or res[-1] != i:
            res.append(i)
    print(len(res))
    print(*res)
