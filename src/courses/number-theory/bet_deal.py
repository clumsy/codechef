t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    diff = (100 - a) - (200 - 2 * b)
    res = "FIRST" if diff < 0 else "SECOND" if diff > 0 else "BOTH"
    print(res)
