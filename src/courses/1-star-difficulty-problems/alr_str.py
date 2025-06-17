t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    z = s.count("0")
    z = min(z, n - z)
    res = z + min(n - z, z + 1)
    print(res)
