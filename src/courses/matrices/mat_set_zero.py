n, m = (int(i) for i in input().split())
mat = [[int(i) for i in input().split()] for _ in range(n)]
rs, cs = set(), set()
for r in range(n):
    for c in range(m):
        if mat[r][c] == 0:
            rs.add(r)
            cs.add(c)
for r in range(n):
    for c in range(m):
        if r in rs or c in cs:
            mat[r][c] = 0
for res in mat:
    print(*res)
