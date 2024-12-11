t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    s = input()
    mi = ma = x
    for c in s:
        x += 1 if c == "R" else -1
        mi = min(mi, x)
        ma = max(ma, x)
    res = ma - mi + 1
    print(res)
