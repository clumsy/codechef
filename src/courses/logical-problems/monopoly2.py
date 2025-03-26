t = int(input())
for _ in range(t):
    p, q, r, s = (int(i) for i in input().split())
    res = "YES" if 2 * max(p, q, r, s) > sum((p, q, r, s)) else "NO"
    print(res)
