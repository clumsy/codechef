t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = x
    for i in a:
        x += i
        res = max(res, x)
    print(res)
