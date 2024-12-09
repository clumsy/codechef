m, n = (int(i) for i in input().split())
mat1 = [[int(i) for i in input().split()] for _ in range(m)]
n, p = (int(i) for i in input().split())
mat2 = [[int(i) for i in input().split()] for _ in range(n)]
res = [[0] * p for _ in range(m)]
for r in range(m):
    for c in range(p):
        for i in range(n):
            res[r][c] += mat1[r][i] * mat2[i][c]
for r in res:
    print(*r)
