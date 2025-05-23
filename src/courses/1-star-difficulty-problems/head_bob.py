t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "NOT INDIAN" if "I" not in s and "Y" in s else "INDIAN" if "I" in s else "NOT SURE"
    print(res)
