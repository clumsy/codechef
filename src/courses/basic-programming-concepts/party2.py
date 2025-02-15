t = int(input())
for _ in range(t):
    n, x, k = (int(i) for i in input().split())
    res = "YES" if k >= n * x else "NO"
    print(res)
