t = int(input())
for _ in range(t):
    x, n = (int(i) for i in input().split())
    res = (x // 10) * n
    print(res)
