t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    cnt, ma = {}, 0
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1
        ma = max(ma, cnt[i])
    res = n - ma
    print(res)
