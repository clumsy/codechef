t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = x % (n + 1)
    print(res)
