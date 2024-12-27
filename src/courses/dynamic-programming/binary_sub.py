mod = 998244353
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    dp = [1] * (n + 1)
    for i in range(1, n):
        dp[i + 1] = (dp[i] + (dp[i - 1] if s[i - 1] != s[i] else 0)) % mod
    res = dp[-1]
    print(res)
