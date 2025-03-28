t = int(input())
for _ in range(t):
    x = int(input())
    res = "LEFT" if 2 * x <= 100 else "RIGHT"
    print(res)
