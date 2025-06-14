t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    d = (int(i) for i in input().split())
    res = "".join("1" if i % k == 0 else "0" for i in d)
    print(res)
