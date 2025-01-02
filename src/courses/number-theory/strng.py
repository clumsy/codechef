from math import gcd


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    g = gcd(*a)
    if g > 1:
        res = n
    else:
        res = 0
        lft, rgt = [a[0]] * n, [a[-1]] * n
        for i in range(1, n):
            lft[i] = gcd(lft[i - 1], a[i])
            rgt[n - 1 - i] = gcd(a[n - 1 - i], rgt[n - 1 - i + 1])
        for i in range(n):
            g = rgt[i + 1] if i == 0 else lft[i - 1] if i == n - 1 else gcd(lft[i - 1], rgt[i + 1])
            res += g > 1
    print(res)
