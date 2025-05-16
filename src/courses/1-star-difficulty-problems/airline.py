t = int(input())
for _ in range(t):
    a, b, c, d, e = (int(i) for i in input().split())
    res = "YES" if (
        (a + b <= d and c <= e) or
        (a + c <= d and b <= e) or
        (b + c <= d and a <= e)
    ) else "NO"
    print(res)
