t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res = max(res, sum(int(d) for d in str(a[i] * a[j])))
    print(res)
