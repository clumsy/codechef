t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    p = [0, 0]
    for i in (a, b, c):
        p[i & 1] += 1
    res = "YES" if p[0] > 0 and p[1] > 0 else "NO"
    print(res)
