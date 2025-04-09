t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    d, r = divmod(n, m)
    res = "YES" if r == d & 1 == 0 else "NO"
    print(res)
