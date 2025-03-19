t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = (n * x + 3) // 4
    print(res)
