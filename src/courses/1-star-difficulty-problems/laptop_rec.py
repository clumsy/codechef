from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt, res = Counter(a), {}
    for k, v in cnt.items():
        res[v] = res.get(v, [])
        res[v].append(k)
    res = res[max(res.keys())]
    res = res[0] if len(res) == 1 else "CONFUSED"
    print(res)
