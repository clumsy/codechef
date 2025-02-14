t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if x >= 2 * y else "NO"
    print(res)
