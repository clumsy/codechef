t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = min(3 * x, 2 * y)
    print(res)
