t = int(input())
for _ in range(t):
    a = (int(i) for i in input().split())
    mi, ma, s = 10001, 0, 0
    for i in a:
        s += i
        mi = min(mi, i)
        ma = max(ma, i)
    res = s - mi - ma
    print(res)
