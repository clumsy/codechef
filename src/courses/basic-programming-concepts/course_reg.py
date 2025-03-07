t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    res = "YES" if m - k >= n else "NO"
    print(res)
