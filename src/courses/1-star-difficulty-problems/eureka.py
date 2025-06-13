t = int(input())
for _ in range(t):
    n = int(input())
    p = res = 1
    v = 0.143 * n
    while p <= n:
        if (n & p) == p:
            res *= v
        v *= v
        p <<= 1
    res = int(res + 0.5)
    print(res)
