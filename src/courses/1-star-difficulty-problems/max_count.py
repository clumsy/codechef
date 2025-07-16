from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    c, v = max((c, -i) for i, c in cnt.items())
    res = -v, c
    print(*res)
