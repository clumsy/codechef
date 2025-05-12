t = int(input())
for _ in range(t):
    s = [input() for _ in range(2)]
    res = [0, 0]
    for c1, c2 in zip(*s):
        if c1 == "?":
            res[1] += 1
        elif c1 != c2:
            res[0] += c2 != "?"
            res[1] += 1
    print(*res)
