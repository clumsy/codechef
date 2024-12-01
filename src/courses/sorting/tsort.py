n = int(input())
a = (int(input()) for _ in range(n))
res = sorted(a)
print(*res, sep="\n")
