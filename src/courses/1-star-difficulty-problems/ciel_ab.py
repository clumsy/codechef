a, b = (int(i) for i in input().split())
res = (a - b) - (a - b) % 10 + (a - b + 1) % 10
res = res if res != 0 else 8
print(res)
