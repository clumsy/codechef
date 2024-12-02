t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    res = ml = mc = 0
    for i, (ai, bi) in enumerate(zip(a, b)):
        if ai >= ml and (ai > ml or bi > mc):
            res = i + 1
            ml, mc = ai, bi
    print(res)
