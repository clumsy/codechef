t = int(input())
for _ in range(t):
    rs = input().split()
    res = "IN" if all(c == "0" for c in rs) else "OUT"
    print(res)
