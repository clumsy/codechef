t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, cur = 0, 1
    for i in range(1, n):
        if a[i] < a[i - 1]:
            res += (1 + cur) * cur // 2
            cur = 0
        cur += 1
    res += (1 + cur) * cur // 2
    print(res)
