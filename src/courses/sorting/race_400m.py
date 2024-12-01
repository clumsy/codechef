t = int(input())
for _ in range(t):
    x, y, z = (int(i) for i in input().split())
    mi = 101
    for t, n in zip((x, y, z), ("Alice", "Bob", "Charlie")):
        if t < mi:
            mi, res = t, n
    print(res)
