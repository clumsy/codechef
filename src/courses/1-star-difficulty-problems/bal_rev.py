t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    zs = s.count("0")
    res = "0" * zs + "1" * (n - zs)
    print(res)
