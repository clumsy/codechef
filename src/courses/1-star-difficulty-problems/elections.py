t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    if a > 50:
        res = "A"
    elif b > 50:
        res = "B"
    elif c > 50:
        res = "C"
    else:
        res = "NOTA"
    print(res)
