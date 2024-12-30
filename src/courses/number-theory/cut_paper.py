t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = (n // k) * (n // k)
    print(res)
