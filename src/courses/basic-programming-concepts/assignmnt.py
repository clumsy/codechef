t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    res = "YES" if z * 60 * 24 >= x * y else "NO"
    print(res)
