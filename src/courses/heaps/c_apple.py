t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res = len(set(a))
    print(res)
