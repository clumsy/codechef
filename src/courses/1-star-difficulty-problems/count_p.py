t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    odd = sum(i & 1 for i in a)
    res = "YES" if odd > 0 and odd & 1 == 0 else "NO"
    print(res)
