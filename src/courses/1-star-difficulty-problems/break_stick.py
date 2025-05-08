t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = "YES" if ((n - x) & 1) == (x & 1) or (n & 1) == (x & 1) else "NO"
    print(res)
