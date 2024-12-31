t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if x ** 4 + 4 * y ** 2 == 4 * x ** 2 * y else "NO"
    print(res)
