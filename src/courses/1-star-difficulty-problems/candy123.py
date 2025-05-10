from math import sqrt, floor


t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    # (1 + x * 2 - 1) * x / 2 = A
    x = floor(sqrt(a))
    # (2 + y * 2) * y / 2 = B
    y = floor((-1 + sqrt(1 + 4 * b)) / 2)
    res = "Limak" if x > y else "Bob"
    print(res)
