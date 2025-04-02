t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    res = max(a, b) + max(c, d)
    print(res)
