t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if y > x else "NO"
    print(res)
