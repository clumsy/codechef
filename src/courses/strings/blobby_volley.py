t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    srv, res = "A", {}
    res["A"] = res["B"] = 0
    for i in s:
        if srv == i:
            res[srv] += 1
        else:
            srv = "B" if srv == "A" else "A"
    res = res["A"], res["B"]
    print(*res)
