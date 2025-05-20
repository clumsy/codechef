t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = "PIZZA" if x >= y else "BURGER" if x >= z else "NOTHING"
    print(res)
