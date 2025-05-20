t = int(input())
for _ in range(t):
    n, a, b = int(input()), *(input() for _ in range(2))
    res = "YES" if a.count("1") == b.count("1") else "NO"
    print(res)
