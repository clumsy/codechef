t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res = "YES" if sum(a) & 1 == 0 else "NO"
    print(res)
