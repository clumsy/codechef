t = int(input())
for _ in range(t):
    d = [int(i) for i in input().split()]
    s = [int(i) for i in input().split()]
    d = [sum(d)] + d
    s = [sum(s)] + s
    res = "TIE" if d == s else "DRAGON" if d > s else "SLOTH"
    print(res)
