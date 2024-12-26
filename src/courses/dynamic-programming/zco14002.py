n = int(input())
s = (int(i) for i in input().split())
dp = [[0] * 3 for _ in range(2)]
for i in range(n):
    dp[(i + 1) % 2][0] = next(s) + dp[i % 2][2]
    dp[(i + 1) % 2][1] = min(dp[i % 2][0], dp[(i + 1) % 2][0])
    dp[(i + 1) % 2][2] = min(dp[i % 2][1], dp[(i + 1) % 2][1])
res = min(dp[n % 2])
print(res)
