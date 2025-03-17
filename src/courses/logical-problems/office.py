t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = 4 * x + y
    print(res)
