n, l, r = (int(i) for i in input().split())
res = (n >> l) << r
print(res)
