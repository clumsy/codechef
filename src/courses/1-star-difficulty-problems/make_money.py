t = int(input())
for _ in range(t):
    n, x, c = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = sum(max(i, x - c) for i in a)
    print(res)
