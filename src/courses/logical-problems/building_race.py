t = int(input())
for _ in range(t):
    a, b, x, y = (int(i) for i in input().split())
    diff = a / x - b / y
    res = "Chefina" if diff > 0 else "Chef" if diff < 0 else "Both"
    print(res)
