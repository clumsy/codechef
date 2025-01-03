t = int(input())
for _ in range(t):
    n, b = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    a = set(a)
    res = 1 if any(i + b in a or i - b in a for i in a) else 0
    print(res)
