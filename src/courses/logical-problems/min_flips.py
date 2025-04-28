t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = -1 if n & 1 == 1 else abs(sum(a) // 2)
    print(res)
