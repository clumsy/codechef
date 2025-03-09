t = int(input())
for _ in range(t):
    w, x, y, z = (int(i) for i in input().split())
    res = w + (x - y) * z
    print(res)
