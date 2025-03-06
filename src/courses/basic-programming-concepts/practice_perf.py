p = (int(i) for i in input().split())
res = sum(i >= 10 for i in p)
print(res)
