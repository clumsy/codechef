t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    for i in range(n):
        res *= i + 1
    print(res)
