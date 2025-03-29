t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    diff = a / 0.1 - b / 0.2
    res = "FIRST" if diff > 0 else "SECOND" if diff < 0 else "ANY"
    print(res)
