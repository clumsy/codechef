t = int(input())
for _ in range(t):
    s = input()
    res = sum(int(c) for c in s if c.isdigit())
    print(res)
