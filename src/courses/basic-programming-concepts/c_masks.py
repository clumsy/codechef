t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "CLOTH" if y <= 10 * x else "DISPOSABLE"
    print(res)
