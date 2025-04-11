t = int(input())
for _ in range(t):
    n, k, m = (int(i) for i in input().split())
    res = (n + k * m - 1) // (k * m)
    print(res)
