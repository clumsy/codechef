t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    for _ in range(n):
        a = int(input())
        res ^= a
    print(res)
