r, o, c = (int(i) for i in input().split())
res = "YES" if 6 * 6 * (20 - o) + c > r else "NO"
print(res)
