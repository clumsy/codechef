t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, ins = 0, set()
    for i in a:
        if i in ins:
            ins.remove(i)
        else:
            ins.add(i)
        res = max(res, len(ins))
    print(res)
