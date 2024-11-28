t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    res = sum(2 * ai >= bi and 2 * bi >= ai for ai, bi in zip(a, b))
    print(res)
