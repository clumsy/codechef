t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = ((n + 1) // 2) * ((m + 1) // 2)
    print(res)
