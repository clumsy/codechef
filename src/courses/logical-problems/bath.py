t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = x // (2 * y)
    print(res)
