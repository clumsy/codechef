t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = []
    for i in a:
        if k >= i:
            res.append("1")
            k -= i
        else:
            res.append("0")
    res = "".join(res)
    print(res)
