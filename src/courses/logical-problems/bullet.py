t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = max(0, z - y // x)
    print(res)
