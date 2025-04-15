t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    res = (n + 1) // 2 * b + n // 2 * a
    print(res)
