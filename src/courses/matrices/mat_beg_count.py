from bisect import bisect_left


n, m = (int(i) for i in input().split())
mat = [[int(i) for i in input().split()] for _ in range(n)]
res = 0
for r in range(n):
    i = bisect_left(mat[r], 1, key=lambda x: -x)
    res += m - i
print(res)
