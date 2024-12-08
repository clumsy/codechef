n, m = (int(i) for i in input().split())
mat = [[int(i) for i in input().split()] for _ in range(n)]
res = []
for r in reversed(range(n)):
    print(*mat[r])
