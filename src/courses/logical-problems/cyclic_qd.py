t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    res = "YES" if a + c == b + d == 180 else "NO"
    print(res)
