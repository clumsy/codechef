n = int(input())
a = (int(i) for i in input().split())
res = "READY FOR BATTLE" if 2 * sum(i & 1 == 0 for i in a) > n else "NOT READY"
print(res)
