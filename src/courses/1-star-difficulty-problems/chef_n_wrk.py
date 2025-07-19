t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, cur = 1, 0
    for i in a:
        if i > k:
            res = -1
            break
        if cur + i > k:
            cur = 0
            res += 1
        cur += i
    print(res)
