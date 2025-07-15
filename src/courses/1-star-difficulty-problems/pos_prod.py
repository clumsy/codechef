t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    pos = neg = 0
    for i in a:
        pos += i > 0
        neg += i < 0
    res = (pos * (pos - 1) + neg * (neg - 1)) // 2
    print(res)
