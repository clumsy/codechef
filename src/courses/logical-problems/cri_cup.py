t = int(input())
for _ in range(t):
    x, y, d = (int(i) for i in input().split())
    res = "YES" if abs(x - y) <= d else "NO"
    print(res)
