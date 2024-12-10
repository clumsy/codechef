n, m = (int(i) for i in input().split())
mat = [[int(i) for i in input().split()] for _ in range(n)]
for r in reversed(range(n)):
    d = min(n - r, m)
    diag = [0] * d
    for k in range(d):
        diag[k] = mat[r + k][k]
    diag.sort()
    for k in range(d):
        mat[r + k][k] = diag[k]
for c in range(1, m):
    d = min(m - c, n)
    diag = [0] * d
    for k in range(d):
        diag[k] = mat[k][c + k]
    diag.sort()
    for k in range(d):
        mat[k][c + k] = diag[k]
for res in mat:
    print(*res)
