t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = abs((x - 1) // 10 - (y - 1) // 10)
    print(res)
