from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, cnt = 0, Counter(a)
    cur, ma = n, max(cnt.keys())
    while cur:
        if ma > cur:
            res = -1
            break
        while cnt[ma] == 0:
            ma -= 1
        if cnt[ma]:
            res += cur - ma
            cnt[ma] -= 1
            ma -= cnt[ma] == 0
            cur -= 1
        else:
            res = -1
            break
    print(res)
