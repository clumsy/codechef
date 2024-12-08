n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]
res = 0
for r in range(n):
    res += mat[r][r] + (mat[r][n - 1 - r] if n - 1 - r != r else 0)
print(res)
