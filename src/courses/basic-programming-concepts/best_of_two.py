t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = max(x, y)
    print(res)
