t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = [1] * n
    for i in reversed(range(n - 1)):
        res[i] = res[i + 1] + 1 if a[i] * a[i + 1] < 0 else 1
    print(*res)
