t = int(input())
for _ in range(t):
    n, p = (int(i) for i in input().split())
    cnt = (int(i) for i in input().split())
    cwk = hrd = 0
    for c in cnt:
        cwk += c >= p // 2
        hrd += c <= p // 10
    res = "yes" if cwk == 1 and hrd == 2 else "no"
    print(res)
