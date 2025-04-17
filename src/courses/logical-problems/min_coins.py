t = int(input())
for _ in range(t):
    x = int(input())
    res = -1 if x % 5 != 0 else x // 10 + (x & 1)
    print(res)
