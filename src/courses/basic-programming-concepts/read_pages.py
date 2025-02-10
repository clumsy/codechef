t = int(input())
for _ in range(t):
    n, x, y = (int(i) for i in input().split())
    res = "YES" if x * y >= n else "NO"
    print(res)
