t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = (y - 1) // x
    print(res)
