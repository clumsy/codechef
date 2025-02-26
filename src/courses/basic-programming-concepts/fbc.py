t = int(input())
for _ in range(t):
    k, x = (int(i) for i in input().split())
    res = k - x
    print(res)
