t = int(input())
m = ["LB", "MB", "UB", "LB", "MB", "UB", "SU", "SL"]
for _ in range(t):
    n = int(input())
    d = (n - 1) % 8
    f = n + 3 if d < 3 else n - 3 if d < 6 else n + 1 if d < 7 else n - 1
    res = f"{f}{m[d]}"
    print(res)
