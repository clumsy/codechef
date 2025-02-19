t = int(input())
for _ in range(t):
    x = int(input())
    res = "MILD" if x < 4 else "MEDIUM" if x < 7 else "HOT"
    print(res)
