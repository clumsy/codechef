t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = "YES" if a == b or b - a >= a else "NO"
    print(res)
