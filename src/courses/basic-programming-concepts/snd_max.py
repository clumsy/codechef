t = int(input())
for _ in range(t):
    a = (int(i) for i in input().split())
    res = [i for i in sorted(a)][1]
    print(res)
