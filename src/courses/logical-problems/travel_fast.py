t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    diff = x - y
    res = "CAR" if diff > 0 else "BIKE" if diff < 0 else "SAME"
    print(res)
