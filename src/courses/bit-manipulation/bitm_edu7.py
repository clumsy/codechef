n = int(input())
res = [-1, n & 1]
ms = 0
while n > 0:
    n >>= 1
    ms += 1
res[0] = ms - 1
print(*res)
