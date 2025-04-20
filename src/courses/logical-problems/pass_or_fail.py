t = int(input())
for _ in range(t):
    n, x, p = (int(i) for i in input().split())
    res = "PASS" if 3 * x - (n - x) >= p else "FAIL"
    print(res)
