t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = 0
    for i in a:
        res += max(abs(i - 1), abs(m - i))
    print(res)
