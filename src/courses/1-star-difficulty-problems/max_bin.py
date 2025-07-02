t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    res = "1" + s[1:] + "0" * (k - (s[0] == "0"))
    print(res)
