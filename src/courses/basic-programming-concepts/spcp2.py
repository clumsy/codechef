t = int(input())
for _ in range(t):
    x, n = (int(i) for i in input().split())
    res = max(0, (n + 99) // 100 - x)
    print(res)
