t = int(input())
for _ in range(t):
    n, b, m = (int(i) for i in input().split())
    res = -b
    while n:
        res += (n + 1) // 2 * m + b
        n //= 2
        m *= 2
    print(res)
