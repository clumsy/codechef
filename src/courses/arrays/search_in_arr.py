n, x = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = "NO"
for i in a:
    if x == i:
        res = "YES"
        break
print(res)
