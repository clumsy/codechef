t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "YES" if max(a, c) <= b else "NO"
    print(res)
