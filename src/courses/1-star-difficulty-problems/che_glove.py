t = int(input())
for _ in range(t):
    n, l = int(input()), [int(i) for i in input().split()]
    g = [int(i) for i in input().split()]
    d1 = [y - x for x, y in zip(l, g)]
    d2 = [y - x for x, y in zip(l, g[::-1])]
    res = "both" if min(d1) >= 0 and min(d2) >= 0 else "front" if min(d1) >= 0 else "back" if min(d2) >= 0 else "none"
    print(res)
