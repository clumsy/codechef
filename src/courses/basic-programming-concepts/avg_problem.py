t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "YES" if (a + b) / 2 > c else "NO"
    print(res)
