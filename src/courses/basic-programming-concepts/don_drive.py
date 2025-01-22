t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = max(0, n - x)
    print(res)
