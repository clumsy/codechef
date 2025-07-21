from collections import Counter


t = int(input())
for _ in range(t):
    s = input().strip()
    cnt = Counter(s)
    res = sum((c + 1) // 2 for c in cnt.values())
    print(res)
