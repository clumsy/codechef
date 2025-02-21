t = int(input())
for _ in range(t):
    x = int(input())
    res = "BRONZE" if x <= 3 else "SILVER" if x <= 6 else "GOLD"
    print(res)
