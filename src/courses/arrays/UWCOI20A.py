t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res = max(a)
    print(res)
