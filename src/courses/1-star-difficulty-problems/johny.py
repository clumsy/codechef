t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    k = int(input())
    res = sum(i <= a[k - 1] for i in a)
    print(res)
