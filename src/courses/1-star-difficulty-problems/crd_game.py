t = int(input())
for _ in range(t):
    n = int(input())
    c = m = 0
    for _ in range(n):
        a, b = input().split()
        d = sum(int(c) for c in a) - sum(int(c) for c in b)
        if d > 0:
            c += 1
        elif d < 0:
            m += 1
        else:
            c += 1
            m += 1
    res = (0, c) if c > m else (1, m) if c < m else (2, c)
    print(*res)
