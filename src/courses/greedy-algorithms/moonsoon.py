t = int(input())
for _ in range(t):
    n, m, h = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    res = 0
    for ai, bi in zip(sorted(a, reverse=True), sorted(b, reverse=True)):
        res += min(ai, h * bi)
    print(res)
