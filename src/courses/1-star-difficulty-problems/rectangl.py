t = int(input())
for _ in range(t):
    a, b, c, d = sorted(int(i) for i in input().split())
    res = "YES" if a == b and c == d else "NO"
    print(res)
