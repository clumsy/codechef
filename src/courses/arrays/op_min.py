t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    mi, cnt = 101, 0
    for i in a:
        if i < mi:
            mi, cnt = i, 1
        elif i == mi:
            cnt += 1
    res = n - cnt
    print(res)
