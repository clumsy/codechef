x, y = (int(i) for i in input().split())
res = min(x, y // 2) + max(0, x - y)
print(res)
