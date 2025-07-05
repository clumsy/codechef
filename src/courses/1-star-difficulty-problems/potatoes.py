prm = [True] * 3000
prm[0] = prm[1] = False
for i in range(len(prm)):
    if prm[i]:
        for j in range(2 * i, len(prm), i):
            prm[j] = False
t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    for i in range(x + y + 1, len(prm)):
        if prm[i]:
            res = i - (x + y)
            break
    print(res)
