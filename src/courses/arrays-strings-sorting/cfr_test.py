t = int(input())
for _ in range(t):
    n = int(input())
    d = (int(i) for i in input().split())
    res = len(set(d))
    print(res)
