t = int(input())
for _ in range(t):
    a, b, x, y = (int(i) for i in input().split())
    res = "YES" if x * y >= a * b else "NO"
    print(res)
