t = int(input())
for _ in range(t):
    n = int(input())
    s = (int(i) for i in input().split())
    p, res = next(s), 0
    for i in s:
        res += abs(i - p) - 1
        p = i
    print(res)
