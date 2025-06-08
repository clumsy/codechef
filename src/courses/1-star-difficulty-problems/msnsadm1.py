t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    res = max(0, max(20 * ai - 10 * bi for ai, bi in zip(a, b)))
    print(res)
