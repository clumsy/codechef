t = int(input())
for _ in range(t):
    n, m, x = (int(i) for i in input().split())
    res = 2 * (m + n) * x
    print(res)
