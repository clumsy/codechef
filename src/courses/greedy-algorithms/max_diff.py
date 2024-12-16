t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    w = [int(i) for i in input().split()]
    w.sort()
    k = min(k, n - k)
    res = sum(w[k:]) - sum(w[:k])
    print(res)

