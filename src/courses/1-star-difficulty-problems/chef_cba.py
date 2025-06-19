a, b, c, d = sorted(int(i) for i in input().split())
res = "Possible" if a / c == b / d else "Impossible"
print(res)
