t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    o = s.count("1")
    res = 0 if not o else min(o, n - o + 1)
    print(res)
