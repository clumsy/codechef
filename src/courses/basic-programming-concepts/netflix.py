t = int(input())
for _ in range(t):
    a, b, c, x = (int(i) for i in input().split())
    res = "YES" if max(a + b, b + c, a + c) >= x else "NO"
    print(res)
