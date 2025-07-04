t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = 0
    for _ in range(n):
        ti, di = (int(i) for i in input().split())
        res += max(0, ti - k) * di
        k = max(0, k - ti)
    print(res)
