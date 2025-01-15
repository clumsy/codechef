t = int(input())
for _ in range(t):
    n = int(input())
    res, n = divmod(n, 2048)
    while n:
        n -= -n & n
        res += 1
    print(res)
