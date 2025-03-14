t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = 2 if z >= x + y else 1 if z >= x else 0
    print(res)
