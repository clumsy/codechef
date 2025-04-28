t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    k = 0
    while n > 1:
        n >>= 1
        k += 1
    res = a * k + b * (k - 1)
    print(res)
