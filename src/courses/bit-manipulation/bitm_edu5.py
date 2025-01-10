n = int(input())
res = 0
while n:
    n -= -n & n
    res += 1
print(res)
