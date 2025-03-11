t = int(input())
for _ in range(t):
    w, x, y, z = (int(i) for i in input().split())
    x -= w + y * z
    res = "filled" if x == 0 else "unfilled" if x > 0 else "overflow"
    print(res)
