t = int(input())
for _ in range(t):
    k, x = (int(i) for i in input().split())
    res = max(0, 7 * k - x)
    print(res)
