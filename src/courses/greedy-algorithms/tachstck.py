n, d = (int(i) for i in input().split())
l = sorted(int(input()) for _ in range(n))
p, res = None, 0
for i in l:
    if p is not None and i - p <= d:
        res += 1
        p = None
    else:
        p = i
print(res)
