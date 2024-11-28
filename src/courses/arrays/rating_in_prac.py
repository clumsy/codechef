t = int(input())
for _ in range(t):
    n, d = int(input()), (int(i) for i in input().split())
    res, prv = "Yes", 0
    for i in d:
        if i < prv:
            res = "No"
            break
        prv = i
    print(res)
