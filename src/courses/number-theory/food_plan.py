t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    diff = n * 0.9 - m
    res = "ONLINE" if diff < 0 else "DINING" if diff > 0 else "EITHER"
    print(res)
