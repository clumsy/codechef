t = int(input())
for _ in range(t):
    x, y, r = (int(i) for i in input().split())
    res = (r // 30 + x + y - 1) // y
    print(res)
