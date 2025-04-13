t = int(input())
for _ in range(t):
    p, q = (int(i) for i in input().split())
    res = "Alice" if ((p + q) // 2) & 1 == 0 else "Bob"
    print(res)
