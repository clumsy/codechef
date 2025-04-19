t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = a + b + c - min(a, b, c) - max(a, b, c)
    print(res)
