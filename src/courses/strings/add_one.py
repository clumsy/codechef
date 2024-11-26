t = int(input())
for _ in range(t):
    n = [int(i) for i in input()]
    c = 1
    for i in reversed(range(len(n))):
        c, n[i] = divmod(n[i] + c, 10)
    n = n if c == 0 else [str(c)] + n
    res = "".join(str(i) for i in n)
    print(res)
