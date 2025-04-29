t = int(input())
for _ in range(t):
    a1, a2, a3, b1, b2, b3 = (int(i) for i in input().split())
    d = ((a1 + a2 + a3) - min(a1, a2, a3)) - ((b1 + b2 + b3) - min(b1, b2, b3))
    res = "Tie" if d == 0 else "Alice" if d > 0 else "Bob"
    print(res)
