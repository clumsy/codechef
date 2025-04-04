t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = min(x, n - x)
    print(res)
