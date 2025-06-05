t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = n - 2 if len(set(s)) != len(s) else -1
    print(res)
