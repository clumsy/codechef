t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    res = sum(bi for ai, bi in zip(a, b) if ai >= x)
    print(res)
