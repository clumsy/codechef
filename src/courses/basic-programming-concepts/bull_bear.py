t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "PROFIT" if y > x else "LOSS" if y < x else "NEUTRAL"
    print(res)
