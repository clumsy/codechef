t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "FIRST" if x < y else "SECOND" if x > y else "ANY"
    print(res)
