t = int(input())
for _ in range(t):
    g = int(input())
    for _ in range(g):
        i, n, q = (int(i) for i in input().split())
        res = n // 2 if n & 1 == 0 else n // 2 if i == q else (n + 1) // 2
        print(res)
