t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if y >= 3 * x else "NO"
    print(res)
