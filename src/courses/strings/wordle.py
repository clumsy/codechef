t = int(input())
for _ in range(t):
    s, t = (input() for _ in range(2))
    res = "".join("G" if si == ti else "B" for si, ti in zip(s, t))
    print(res)
