t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = sorted(a)[-x] - 1
    print(res)
