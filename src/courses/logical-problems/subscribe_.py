t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = (n + 5) // 6 * x
    print(res)
