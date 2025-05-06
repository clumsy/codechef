from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "YES" if max(Counter(a).values()) < 3 else "NO"
    print(res)
