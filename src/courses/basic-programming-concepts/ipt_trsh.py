t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = max(0, n - m)
    print(res)
