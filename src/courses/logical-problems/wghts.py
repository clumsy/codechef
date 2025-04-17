t = int(input())
for _ in range(t):
    w, x, y, z = (int(i) for i in input().split())
    res = "YES" if w in [x, y, z, x + y, y + z, x + z, x + y + z] else "NO"
    print(res)
