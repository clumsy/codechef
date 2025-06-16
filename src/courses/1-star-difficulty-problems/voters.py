from collections import Counter


n = (int(i) for i in input().split())
cnt = Counter()
for _ in range(sum(n)):
    i = int(input())
    cnt[i] += 1
res = sorted(i for i, v in cnt.items() if v > 1)
print(len(res))
print(*res, sep="\n")
