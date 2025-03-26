t = int(input())
for _ in range(t):
    n = int(input())
    ds = (int(i) for i in input().split())
    res = sum(d >= 1000 for d in ds)
    print(res)
