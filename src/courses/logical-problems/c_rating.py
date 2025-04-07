t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = (y - x + 7) // 8
    print(res)
