t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = abs(x - y)
    print(res)
