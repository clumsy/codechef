t = int(input())
for _ in range(t):
    g, b = (int(i) for i in input().split())
    res = b - min(g, b)
    print(res)
