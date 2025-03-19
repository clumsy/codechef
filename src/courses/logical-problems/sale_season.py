t = int(input())
for _ in range(t):
    x = int(input())
    res = x if x <= 100 else x - 25 if x <= 1000 else x - 100 if x <= 5000 else x - 500
    print(res)
