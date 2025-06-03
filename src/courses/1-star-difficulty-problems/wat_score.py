t = int(input())
for _ in range(t):
    n = int(input())
    cnt = {}
    for i in range(n):
        p, s = (int(i) for i in input().split())
        if p < 9:
            cnt[p] = max(s, cnt.get(p, 0))
    res = sum(cnt.values())
    print(res)
