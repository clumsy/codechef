t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "Alice" if a > max(b, c) else "Bob" if b > max(a, c) else "Charlie"
    print(res)
