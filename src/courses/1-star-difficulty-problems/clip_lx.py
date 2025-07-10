t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    # a * 1 + b * 2 = x
    # a + b = y =>
    # b = y - a =>
    # a * 1 + (y - a) * 2 = x =>
    # a * (1 - 2) = x - y * 2 =>
    # a = y * 2 - x
    a = y * 2 - x
    res = max(0, y - a)
    print(res)
