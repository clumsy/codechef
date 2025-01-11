n = int(input())
res = ((n | 1 << 0) & ~(1 << 1)) ^ (1 << 2)
print(res)
