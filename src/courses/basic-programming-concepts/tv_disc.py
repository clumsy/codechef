t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    diff = (a - c) - (b - d)
    res = "FIRST" if diff < 0 else "SECOND" if diff > 0 else "ANY"
    print(res)
