n = int(input())
i = 0
while (1 << i) <= n:
    if (1 << i) & n == (1 << i):
        msb = i
    i += 1
res = n
res ^= (1 << msb)
res ^= 1
print(res)
