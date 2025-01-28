t = int(input())
for _ in range(t):
    n = int(input())
    res = "YES" if n & 1 == 0 else "NO"
    print(res)
