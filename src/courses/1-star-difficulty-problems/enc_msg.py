t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    s = "".join(s[i + 1] + s[i] for i in range(0, n - 1, 2)) + (s[-1] if n & 1 == 1 else "")
    res = "".join(chr(ord("z") - (ord(c) - ord("a"))) for c in s)
    print(res)
