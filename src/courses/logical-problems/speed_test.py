t = int(input())
for _ in range(t):
    a, x, b, y = (int(i) for i in input().split())
    d = a / x - b / y
    res = "EQUAL" if d == 0 else "ALICE" if d > 0 else "BOB"
    print(res)
