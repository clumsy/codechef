t = int(input())
for _ in range(t):
    n, x, k = (int(i) for i in input().split())
    res = min(n, k // x)
    print(res)
