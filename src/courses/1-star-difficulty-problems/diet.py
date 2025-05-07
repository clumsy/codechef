t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res, s = ["YES"], 0
    for i in range(n):
        s = s + a[i] - k
        if s < 0:
            res = "NO", i + 1
            break
    print(*res)
