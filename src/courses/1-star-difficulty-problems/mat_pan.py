t = int(input())
for _ in range(t):
    p, s = [int(i) for i in input().split()], input()
    res = max(0, sum(p) - sum(p[ord(c) - ord("a")] for c in set(s)))
    print(res)
