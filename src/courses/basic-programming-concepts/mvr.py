a, b, x, y = (int(i) for i in input().split())
d = 2 * a + b - 2 * x - y
res = "Messi" if d > 0 else "Ronaldo" if d < 0 else "Equal"
print(res)
