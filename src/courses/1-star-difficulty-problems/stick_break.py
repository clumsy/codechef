t = int(input())
for _ in range(t):
    l, k = (int(i) for i in input().split())
    res = 0 if l % k == 0 else 1
    print(res)
