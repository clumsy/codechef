t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = (max(0, n - x) + 3) // 4
    print(res)
