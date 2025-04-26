t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = sum((i + k) % 7 == 0 for i in a)
    print(res)
