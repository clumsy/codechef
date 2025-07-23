t = int(input())
for _ in range(t):
    n, b = int(input()), [int(i) for i in input().split()]
    s = sum(b) // (n + 1)
    res = [i - s for i in b]
    print(*res)
