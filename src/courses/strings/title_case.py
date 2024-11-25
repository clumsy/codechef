def solve(s):
    res = []
    for c in s.split():
        if c == c.upper():
            res.append(c)
        else:
            res.append(c[0].upper() + c[1:].lower())
    return " ".join(res)

t = int(input())
for _ in range(t):
    s = input()
    res = solve(s)
    print(res)
