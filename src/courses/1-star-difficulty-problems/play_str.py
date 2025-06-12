t = int(input())
for _ in range(t):
    n, s, r = int(input()), input(), input()
    res = "YES" if s.count("1") == r.count("1") else "NO"
    print(res)
