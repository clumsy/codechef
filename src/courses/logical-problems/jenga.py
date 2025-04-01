t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    res = "YES" if x % n == 0 else "NO"
    print(res)
