t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res = cur = sum(a[:k])
    for i in range(k, n):
        cur = cur + a[i] - a[i - k]
        res = max(res, cur)
    print(res)
