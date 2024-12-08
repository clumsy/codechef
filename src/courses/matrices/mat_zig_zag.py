n, m = (int(i) for i in input().split())
mat = [[int(i) for i in input().split()] for _ in range(n)]
res = []
for r in range(n):
    for c in range(m):
        res.append(mat[r][c] if r & 1 == 0 else mat[r][m - 1 - c])
print(*res)
