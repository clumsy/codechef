t = int(input())
for _ in range(t):
    a = int(input())
    res = "Alice" if a % 14 == 0 else "Bob" if a % 9 == 0 and a & 1 == 1 else "Charlie"
    print(res)
