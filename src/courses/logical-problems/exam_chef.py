t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = "YES" if z > x * y / 2 else "NO"
    print(res)
