t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = max(0, x - y)
    print(res)
