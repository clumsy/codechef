t = int(input())
for _ in range(t):
    n = int(input())
    s = [[int(i) for i in input().split()] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            s[r][c] += max(s[r - 1][c], s[r][c - 1]) if r and c else s[r - 1][c] if r else s[r][c - 1] if c else 0
    res = s[n - 1][n - 1] / (n + n - 1 - 2)
    res = "Bad Judges" if res < 0 else res
    print(res)
