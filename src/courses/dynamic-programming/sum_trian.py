t = int(input())
for _ in range(t):
    n, res = int(input()), []
    for i in range(n):
        a = [int(k) for k in input().split()]
        res = [max((res[j - 1] if 0 <= j - 1 < len(res) else 0) + a[j], (res[j] if 0 <= j < len(res) else 0) + a[j]) for j in range(i + 1)]
    res = max(res)
    print(res)
