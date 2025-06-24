from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    res = "YES" if all(v & 1 == 0 for v in cnt.values()) else "NO"
    print(res)
