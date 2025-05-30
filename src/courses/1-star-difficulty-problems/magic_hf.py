t = int(input())
for _ in range(t):
    n, x, s = (int(i) for i in input().split())
    for _ in range(s):
        a, b = (int(i) for i in input().split())
        if b == x:
            x = a
        elif a == x:
            x = b
    res = x
    print(res)
