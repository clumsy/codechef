t = int(input())
for _ in range(t):
    a, b, x = (int(i) for i in input().split())
    res = "YES" if (max(a, b) - min(a, b)) % (2 * x) == 0 else "NO"
    print(res)
