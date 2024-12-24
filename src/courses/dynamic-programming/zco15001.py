n, s = int(input()), [int(i) for i in input().split()]
# dp[i] - how many cuts needed for s[:i]
dp = [0 if i == 0 else float("inf") for i in range(n + 1)]
for e in range(1, n + 1):
    for b in range(e):
        if s[b:e] == s[b:e][::-1]:
            # b:e is a palindrome, so res = the number of cuts needed for s[:b] + this cut
            dp[e] = min(dp[e], dp[b] + 1)
res = dp[n]
print(res)

# from functools import lru_cache
#
# @lru_cache
# def solve(s):
#     if s == s[::-1]:
#         return 1
#     res = len(s)
#     for i in range(1, res):
#         if s[:i] == s[:i][::-1]:
#             res = min(res, 1 + solve(s[i:]))
#     return res
#
# n, s = int(input()), tuple(int(i) for i in input().split())
# res = solve(s)
# print(res)
