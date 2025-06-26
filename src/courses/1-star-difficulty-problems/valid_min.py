t = int(input())
for _ in range(t):
    a, b, c = sorted(int(i) for i in input().split())
    res = "YES" if a == b else "NO"
    print(res)
