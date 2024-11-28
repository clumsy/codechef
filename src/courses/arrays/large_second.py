t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    ma1 = ma2 = 0
    for i in a:
        if i > ma1:
            ma1, ma2 = i, ma1
        elif ma1 > i > ma2:
            ma2 = i
    res = ma1 + ma2
    print(res)
