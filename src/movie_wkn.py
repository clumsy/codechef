t = int(input())
for _ in range(t):
    n = int(input())
    l = (int(i) for i in input().split())
    r = (int(i) for i in input().split())
    max_lr = max_r = 0
    for i, (li, ri) in enumerate(zip(l, r)):
        if li * ri > max_lr:
            max_lr = li * ri
            max_r = ri
            res = i + 1
        elif li * ri == max_lr:
            if ri > max_r:
                max_r = ri
                res = i + 1
    print(res)
