n = int(input())
res = []
while n:
    n, r = divmod(n, 2)
    res.append(str(r))
res = "".join(reversed(res))
print(res)
