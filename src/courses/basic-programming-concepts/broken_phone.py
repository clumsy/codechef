t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "ANY" if x == y else "REPAIR" if x < y else "NEW PHONE"
    print(res)
