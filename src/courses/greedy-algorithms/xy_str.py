t = int(input())
for _ in range(t):
    s = input()
    res, i = 0, 1
    while i < len(s):
        if s[i - 1] != s[i]:
            res += 1
            i += 1
        i += 1
    print(res)
