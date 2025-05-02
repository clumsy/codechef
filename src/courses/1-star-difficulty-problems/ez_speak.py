vwls = "aeiou"
t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    cur = 0
    for c in s:
        if c in vwls:
            cur = 0
        else:
            cur += 1
            if cur >= 4:
                break
    res = "NO" if cur >= 4 else "YES"
    print(res)
