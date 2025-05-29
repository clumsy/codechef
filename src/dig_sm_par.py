t = int(input())
for _ in range(t):
    n = int(input())
    d = sum(int(c) for c in str(n)) & 1
    while True:
        n += 1
        if (sum(int(c) for c in str(n)) & 1) != d:
            res = n
            break
    print(res)
