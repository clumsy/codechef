n, k = (int(i) for i in input().split())
res = 0
for _ in range(n):
    a = int(input())
    res += a % k == 0
print(res)
