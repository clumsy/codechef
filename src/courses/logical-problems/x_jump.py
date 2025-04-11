t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = sum(divmod(x, y))
    print(res)
