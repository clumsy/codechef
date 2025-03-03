t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if x >= 30 * y else "NO"
    print(res)
