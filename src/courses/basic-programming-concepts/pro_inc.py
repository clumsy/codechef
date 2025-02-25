t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = (10 * x) // 100 + y
    print(res)
