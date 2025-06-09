from collections import Counter


t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    cnt = Counter(s)
    res = "YES" if all(v & 1 == 0 for v in cnt.values()) else "NO"
    print(res)
