t = int(input())
for _ in range(t):
    a, b, x, y = (int(i) for i in input().split())
    diff = b - a
    res = "YES" if (x >= diff and diff >= 0) or (y >= -diff and diff < 0) else "NO"
    print(res)
