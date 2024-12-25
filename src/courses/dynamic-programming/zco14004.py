n = int(input())
m = (int(i) for i in input().split())
res = p = 0
dp = []
for i in m:
    res = max(res, i + (dp[-3] if len(dp) > 2 else 0) + p, i + (dp[-2] if len(dp) > 1 else 0))
    p = i
    dp.append(res)
print(res)
