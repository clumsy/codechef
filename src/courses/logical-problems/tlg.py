n = int(input())
ma = s = t = 0
for _ in range(n):
    si, ti = (int(i) for i in input().split())
    s, t = s + si, t + ti
    cur = abs(s - t)
    if cur > ma:
        ma = cur
        res = 1 if s > t else 2
print(res, ma)
