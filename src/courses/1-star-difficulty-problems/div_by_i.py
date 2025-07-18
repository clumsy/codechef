from itertools import zip_longest


t = int(input())
for _ in range(t):
    n = int(input())
    res = (i for a, b in zip_longest(range(n // 2 + 1, n + 1), range(n // 2, 0, -1)) for i in (a, b) if i is not None and i > 0)
    print(*res)
