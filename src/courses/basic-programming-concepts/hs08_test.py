x, y = input().split()
x, y = int(x), float(y)
res = y - x - 0.5 if x % 5 == 0 and y - x - 0.5 >= 0 else y
print(res)
