t = int(input())
for _ in range(t):
    n, x, y = (int(i) for i in input().split())
    d, r = divmod(y, x)
    res = "YES" if n >= d and r == 0 else "NO"
    print(res)
