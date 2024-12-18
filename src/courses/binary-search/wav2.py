from bisect import bisect_left


n, q = (int(i) for i in input().split())
a = (int(i) for i in input().split())
a = sorted(list(a))
for _ in range(q):
    i = int(input())
    neg = bisect_left(a, i)
    res = 0 if neg < n and a[neg] == i else "POSITIVE" if neg & 1 == 0 else "NEGATIVE"
    print(res)
