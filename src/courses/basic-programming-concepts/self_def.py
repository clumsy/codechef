t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = sum(10 <= i <= 60 for i in a)
    print(res)
