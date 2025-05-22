t = int(input())
for _ in range(t):
    n, a = (int(i) for i in input().split())
    res = min(a, n - a)
    print(res)
