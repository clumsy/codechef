t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    d = a - b
    res = ">" if d > 0 else "<" if d < 0 else "="
    print(res)
