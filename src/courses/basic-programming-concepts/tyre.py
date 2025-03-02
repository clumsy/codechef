t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = 2 * n + 4 * m
    print(res)
