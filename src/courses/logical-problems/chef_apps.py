t = int(input())
for _ in range(t):
    s, x, y, z = (int(i) for i in input().split())
    res = 0 if s - (x + y) >= z else 1 if s - min(x, y) >= z else 2
    print(res)
