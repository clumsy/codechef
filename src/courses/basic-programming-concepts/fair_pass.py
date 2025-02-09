t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = "YES" if k >= n + 1 else "NO"
    print(res)
