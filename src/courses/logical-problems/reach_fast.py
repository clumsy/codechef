t = int(input())
for _ in range(t):
    a, b, k = (int(i) for i in input().split())
    res = (abs(a - b) + k - 1) // k
    print(res)
