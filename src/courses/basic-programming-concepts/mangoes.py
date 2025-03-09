t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = (z - y) // x
    print(res)
