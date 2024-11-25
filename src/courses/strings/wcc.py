t = int(input())
for _ in range(t):
    x, s = int(input()), input()
    c = d = 0
    for i in s:
        c += i == "C"
        d += i == "D"
    n = len(s)
    dff = c - (n - c - d)
    res = 60 * x if dff > 0 else 55 * x if dff == 0 else 40 * x
    print(res)
