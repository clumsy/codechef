t = int(input())
for _ in range(t):
    x = int(input())
    res = "LIGHT" if x < 3 else "MODERATE" if x < 7 else "HEAVY"
    print(res)
