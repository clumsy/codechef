t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = (5 * x + 10 * y) // z
    print(res)
