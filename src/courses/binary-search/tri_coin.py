from math import floor, sqrt


t = int(input())
for _ in range(t):
    n = int(input())
    # k*(1 + k)/2 = n
    # k^2 + k - 2n = 0
    # k = (-1 + sqrt(1 + 8n))/2
    res = floor((sqrt(1 + 8 * n) - 1) / 2)
    print(res)
