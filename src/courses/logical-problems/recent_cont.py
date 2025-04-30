t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    res = [0] * 2
    for i in a:
        res[1 if i == "LTIME108" else 0] += 1
    print(*res)
