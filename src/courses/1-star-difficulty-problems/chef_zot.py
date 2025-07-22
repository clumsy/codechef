n = int(input())
a = (int(i) for i in input().split())
res = p = -1
for i, e in enumerate(a):
    if e == 0 or i == n - 1:
        res, p = max(res, i - (e == 0) - p), i
print(res)
