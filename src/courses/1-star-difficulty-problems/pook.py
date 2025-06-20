# x....
# ..x..
# ....x
# .x...
# ...x.
t = int(input())
for _ in range(t):
    n = int(input())
    res = max(1, n - 1) if n < 4 else n
    print(res)
