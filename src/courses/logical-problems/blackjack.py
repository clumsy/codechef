t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    diff = 21 - (a + b)
    res = diff if 10 >= diff > 0 else -1
    print(res)
