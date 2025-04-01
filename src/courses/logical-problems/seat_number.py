t = int(input())
for _ in range(t):
    n = int(input())
    lu = "Lower" if n < 16 else "Upper"
    n -= 15 if n > 15 else 0
    sd = "Double" if n < 11 else "Single"
    res = f"{lu} {sd}"
    print(res)
