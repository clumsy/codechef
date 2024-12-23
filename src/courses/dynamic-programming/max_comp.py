from collections import defaultdict


t = int(input())
for _ in range(t):
    n = int(input())
    events = defaultdict(list)
    for _ in range(n):
        s, e, c = (int(i) for i in input().split())
        events[s].append([e, c])
    res, ma = 0, [0] * 49
    for s in range(49):
        res = max(res, ma[s])
        for e, c in events[s]:
            ma[e] = max(ma[e], res + c)
    print(res)
