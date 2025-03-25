t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    c, d = (int(i) for i in input().split())
    res = "POSSIBLE" if a <= c and b <= d else "IMPOSSIBLE"
    print(res)
