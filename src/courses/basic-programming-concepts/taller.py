t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = "B" if b > a else "A"
    print(res)
