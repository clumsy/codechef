t = int(input())
for _ in range(t):
    x, a, b = (int(i) for i in input().split())
    res = "Qualify" if a + 2 * b >= x else "NotQualify"
    print(res)
