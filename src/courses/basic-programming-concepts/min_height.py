t = int(input())
for _ in range(t):
    x, h = (int(i) for i in input().split())
    res = "YES" if x >= h else "NO"
    print(res)
