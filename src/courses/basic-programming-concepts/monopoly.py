t = int(input())
for _ in range(t):
    r1, r2, r3 = (int(i) for i in input().split())
    res = "YES" if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2 else "NO"
    print(res)
