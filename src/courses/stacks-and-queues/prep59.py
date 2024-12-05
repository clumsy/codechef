t = int(input())
for _ in range(t):
    s = input()
    res = int(s[0] == "(" and s[-1] == ")")
    if res:
        o = c = 0
        for i in s:
            if i == "(":
                o += 1
            else:
                c += 1
            if o - c < 0:
                res = 0
                break
        else:
            if o != c:
                res = 0
    print(res)
