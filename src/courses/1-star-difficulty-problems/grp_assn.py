t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1
    res = "YES" if all(cnt[i] % i == 0 for i in cnt) else "NO"
    print(res)
