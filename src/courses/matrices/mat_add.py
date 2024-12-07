n, m = (int(i) for i in input().split())
a = [[int(i) for i in input().split()] for _ in range(n)]
b = [[int(i) for i in input().split()] for _ in range(n)]
c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]
for res in c:
    print(*res)
