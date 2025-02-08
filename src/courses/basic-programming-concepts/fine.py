t = int(input())
for _ in range(t):
    x = int(input())
    res = 2000 if x > 100 else 500 if x > 70 else 0
    print(res)
