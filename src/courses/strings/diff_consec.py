t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = sum(s[i] == s[i - 1] for i in range(1, n))
    print(res)
