from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    cnt = list(Counter(a).values())
    res = "YES" if cnt.count(max(cnt)) == 1 else "NO"
    print(res)
